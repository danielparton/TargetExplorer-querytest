from flask import jsonify, request, make_response
from flaskapp import app, db, models

# ======
# Get multiple database entries given a query string
# ======

# = Example data types from the table 'UniProt' =
# id: [1, 2, 3, ...]
# family: ['CK1', 'AGC', 'TK', ...]
# taxon_name_common: ['Human', 'Mouse', 'Bovine', ...]

# = Example API query strings =
# family=CK1
# family=CK1 && id<1000
# family=CK1 || (family=AGC && taxon_name_common=Human)
# family=CK1 || ((family=AGC || family=TK) && taxon_name_common=Human)
# (many other data types will eventually need to be queryable)

# = Other syntax =
# Equality/relational operators: =, !=, >, <, >=, <=
# Eventually: regex text searching

# = Example URL request with curl =
# curl localhost:5000'/search?query=family=CK1 && id<1000'

@app.route('/search', methods = ['GET'])
def query_db():
    query_string = request.args.get('query')

    valid_fields = ['family', 'taxon_name_common', 'id']

    results_obj = []

    # Parse query_string, check all fields are valid, and convert into sql_query_string
    # TODO



    # Example SQL query strings:
    # sql_query_string="family='CK1' and id<1000"
    sql_query_string="family='CK1' or ((family='AGC' or family='TK') and taxon_name_common='Human')"

    query = db.session.query(models.UniProt).filter(sql_query_string)
    query_rows = query.all()

    # return a string containing basic information about the query results
    for query_row in query_rows:
        results_obj.append('%d %s %s' % (query_row.id, query_row.family, query_row.taxon_name_common))

    return '\n'.join(results_obj) + '\n'
