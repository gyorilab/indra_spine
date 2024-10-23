import os

from flask import Flask, Response, abort, jsonify, render_template, request
from flask_restx import Api, Resource, fields
from indra.literature import pubmed_client

from .process import get_agents, get_network_edges, get_nice_cx_network

app = Flask(__name__)
app.config['RESTX_MASK_SWAGGER'] = False
app.config['SWAGGER_UI_DOC_EXPANSION'] = 'list'


def get_agent_dict():
    agent_dict = {}
    for doc_path, agents in get_agents().items():
        pmid = os.path.splitext(os.path.basename(doc_path))[0]
        agent_dict[pmid] = agents
    return agent_dict


agents = {
    'pubmed_fatigue': get_agent_dict()
}

# NOTE: the Flask REST-X API has to be declared here, below the home endpoint
# otherwise it reserves the / base path.

api = Api(app,
          title="INDRA SPINE service",
          description="INDRA SPINE service",
          version='1.0',
          contact="INDRA labs",
          contact_email="indra.sysbio@gmail.com",
          contact_url="https://indralab.github.io",
          )


base_ns = api.namespace('INDRA SPINE API', 'INDRA SPINE API', path='/')

dict_model = api.model('dict', {})
class_model = \
    api.model('Class',
              {'name': fields.String(description="Name of the class.",
                                     example="corpus callosum"),
               'iri': fields.String(description="IRI of the class.",
                                    example='https://identifiers.org/FMA:63189')})

build_graph_input_model = api.model(
    "BuildGraphInput",
    {
        'databases': fields.List(fields.String, example=['pubmed'],
                                 description="List of databases to use.",
                                 required=True),
        'terms': fields.List(fields.String, example=['fatigue'],
                             description="List of search/topic terms.",
                             required=True),
        'name_search': fields.String(example='pubmed_fatigue',
                                     description="Name for this search context.",
                                     required=True),
    }
)


get_network_input_model = api.model(
    "GetNetworkInput",
    {
        'name_search': fields.String(example='pubmed_fatigue',
                                     description="Name for the search context.",
                                     required=True),
        'classes': fields.List(fields.Nested(class_model), required=False),
    }
)


@base_ns.route('/build_graph', methods=['POST'])
class BuildGraph(Resource):
    @base_ns.response(200, "Build graph response", {})
    @base_ns.expect(build_graph_input_model)
    def post(self):
        pmids = set()
        for term in request.json.get('terms', []):
            pmids |= set(pubmed_client.get_ids(term))
        if not pmids:
            abort(400, 'No PMIDs found for the given terms.')
        agents[request.json['name_search']] = {
            k: v for k, v in agents['pubmed_fatigue'].items() if k in pmids
        }
        return jsonify({})


@base_ns.route('/get_network', methods=['POST'])
class GetNetwork(Resource):
    @base_ns.response(200, "Get network response", {})
    @base_ns.expect(get_network_input_model)
    def post(self):
        name_search = request.json['name_search']
        agents_search = agents.get(name_search)
        if not agents_search:
            abort(400, 'No search context found with the given name.')
        classes = request.json.get('classes')
        edges = get_network_edges(agents_search, classes)
        if not edges:
            abort(400, 'No edges found for the given search.')
        network = get_nice_cx_network(edges)
        cx = network.to_cx()
        return jsonify(cx)


if __name__ == '__main__':
    app.run()
