exports = function({ query, headers, body}, response) {
  const clstr = "mongodb-atlas";
  const dtbs = "customerX";
  const cllctn = "funnel";
  const doc = context.services.get(clstr).db(dtbs).collection(cllctn).aggregate([{ $sample: { size: 1 } }]).toArray()
    .then(arr => {return arr[0]})
  return  doc;
};
