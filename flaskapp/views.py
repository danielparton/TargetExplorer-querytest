from flask import jsonify, request, make_response
from flaskapp import app, db, models

# Example data types
# ------------------
# UniProt.family: ['CK1', 'AGC', 'TK', ...]
# UniProt.taxon_name_common: ['Human', 'Mouse', 'Bovine', ...]
# UniProtDomain.length: [270, 255, 255, 260, ...]

# Example API query strings (SQLAlchemy syntax)
# ---------------------------------------------
# 'family="TK"'
# 'family="TK" and length<270'
# 'family="TK" and taxon_name_common="Human" and domain_length<270'

# This dictionary maps frontend data fields (e.g. 'family') to 2-element lists
# (e.g. ['UniProt', 'family']), which represent the backend table name,
# followed by the column name.
data_mappings_frontend2backend = {
    'family': ['UniProt', 'family'],
    'species': ['UniProt', 'taxon_name_common'],
    'domain_length': ['UniProtDomain', 'length'],
}

# ======
# Get multiple database entries given a query string
# ======

@app.route('/search', methods = ['GET'])
def query_db():
    # query_string = request.args.get('query')

    # Example API query strings
    # input_string = 'family="TK"'
    input_string = 'family="TK" and domain_length<270'
    # input_string = 'family="TK" and species="Human" and domain_length<260'

    # TODO Convert the frontend data fields to backend identifiers '[table].[column]'
    # Determine which tables will need to be queried
    # Start with the DBEntry table, then carry out SQL joins with the other tables
    # Use the query string to filter the DBEntry rows
    # Return results in JSON format (just print results for now)

    # An instructive example showing SQLAlchemy functionality:
    query = db.session.query(models.DBEntry).join(models.UniProt, models.DBEntry.id == models.UniProt.dbentry_id).filter('UniProt.family="TK"')
    print query.all()



    # # Output
    # for dbentry_row in query.all():
    #     uniprot_row = dbentry_row.uniprot.first()
    #     uniprot_domain_rows = dbentry_row.uniprotdomains
    #     uniprot_domain_lengths = [domain.length for domain in uniprot_domain_rows]
    #     output_string = '%d %s %s %r' % (dbentry_row.id, uniprot_row.entry_name, uniprot_row.family, uniprot_domain_lengths)
    #     print output_string
