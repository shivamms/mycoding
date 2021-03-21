import sqlGenerator as sg 

input = {
  "type": "select",
  "columns": ["t1.a", "t2.a", "t2.b"],
  "tables": ["t1", "t2",],
  "wherePredicate": ["t1.a = 'xyz' and ",
                    "t2.a = 'y'"]
}

sg.generate(input)