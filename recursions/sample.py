
def inception(counter):
  if counter > 3:
    return "done"
  counter += 1
  return inception(counter)

