import json

def generate(input):
  sql = []
  sql.append("{} ".format(input["type"]))
  for c in input["columns"]:
    sql.append("{}, ".format(c))
  sql[len(sql)-1] = sql[len(sql)-1][:-2]
  sql.append("from ")
  for t in input["tables"]:
    sql.append("{}, ".format(t))
  sql[len(sql)-1] = sql[len(sql)-1][:-2]
  if input["wherePredicate"]:
    sql.append("where ")
    for p in input["wherePredicate"]:
      sql.append("{} ".format(p))
  query = "\n".join(l for l in sql)
  print(query)
