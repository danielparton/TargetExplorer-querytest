from flask import jsonify, request, make_response
from flaskapp import app, db, models

# ======
# Get multiple database entries given a query string
# ======

# Example data types
# ------------------
# UniProt.family: ['CK1', 'AGC', 'TK', ...]
# UniProt.taxon_name_common: ['Human', 'Mouse', 'Bovine', ...]
# UniProtDomain.length: [270, 255, 255, 260, ...]

# Example API query strings
# -------------------------
# 'UniProt.family="TK"'
# 'UniProt.family="TK" && UniProtDomain.length<270'
# 'UniProt.family="TK" && UniProt.taxon_name_common="Human" && UniProtDomain.length<270'

# Limited set of operators (for now)
# ----------------------------------
# &&, =, >, <

@app.route('/search', methods = ['GET'])
def query_db():
    # query_string = request.args.get('query')

    # Example API query strings
    # query_string = 'UniProt.family="TK"'
    query_string = 'UniProt.family="TK" && UniProtDomain.length<270'
    # query_string = 'UniProt.family="TK" && UniProt.taxon_name_common="Human" && UniProtDomain.length<260'

    # TODO divide the query_string into individual statements (e.g. 'UniProt.family="TK"')
    # use each statement to carry out a separate query of the SQL database
    # combine the results and return (or print)

    # Some instructive examples of SQLAlchemy functionality:
    query1 = db.session.query(models.DBEntry).join(models.UniProt).filter('family="TK"')
    print query1.all()
    # queries_combined = query1.intersect(query2, query3)



    # # Output
    # for dbentry_row in results.all():
    #     uniprot_row = dbentry_row.uniprot.first()
    #     uniprot_domain_rows = dbentry_row.uniprotdomains
    #     uniprot_domain_lengths = [domain.length for domain in uniprot_domain_rows]
    #     output_string = '%d %s %s %r' % (dbentry_row.id, uniprot_row.entry_name, uniprot_row.family, uniprot_domain_lengths)
    #     print output_string

