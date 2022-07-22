import pickle
from flask import Flask, Response, abort, jsonify, render_template, request
from flask_restx import Api, Resource, fields

from indra_spine.process import get_agents, get_network_edges, get_nice_cx_network

app = Flask(__name__)
app.config['RESTX_MASK_SWAGGER'] = False
app.config['SWAGGER_UI_DOC_EXPANSION'] = 'list'

agents = {
    'pubmed_fatigue': get_agents()
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
          #doc='/apidocs',
          )


base_ns = api.namespace('INDRA SPINE API', 'INDRA SPINE API', path='/')

dict_model = api.model('dict', {})
classes_model = \
    api.model('Classes',
              {'classes': fields.List(fields.Nested(dict_model),
                                      example=[{'name': 'corpus callosum',
                                                'iri': 'https://bioregistry.io/fma:63189'}])})

build_graph_input_model = api.model(
    "BuildGraphInput",
    {
        'databases': fields.List(fields.String, example=['pubmed'],
                                 description="List of databases to use."),
        'terms': fields.List(fields.String, example=['fatigue'],
                             description="List of search/topic terms."),
        'name_search': fields.String(example='pubmed_fatigue',
                                     description="Name for this search context."),
    }
)


get_network_input_model = api.model(
    "GetNetworkInput",
    {
        'name_search': fields.String(example='pubmed_fatigue',
                                     description="Name for the search context."),
        'classes': classes_model
    }
)


@base_ns.route('/build_graph', methods=['POST'])
class BuildGraph(Resource):
    @base_ns.response(200, "Build graph response", {})
    @base_ns.expect(build_graph_input_model)
    def post(self):
        return jsonify({})


@base_ns.route('/get_network', methods=['POST'])
class GetNetwork(Resource):
    @base_ns.response(200, "Get network response", {})
    @base_ns.expect(get_network_input_model)
    def post(self):
        name_search = request.json['name_search']
        agents_search = agents.get(name_search)
        breakpoint()
        if not agents_search:
            return jsonify({})
        classes = request.json.get('classes')
        edges = get_network_edges(agents_search, classes)
        network = get_nice_cx_network(edges)
        cx = network.to_cx()
        return jsonify(cx)


if __name__ == '__main__':
    app.run()
