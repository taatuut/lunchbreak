exports = function({ query, headers, body}, response) {
    //const doc = context.services.get("ez-Free-Cluster").db("customerX").collection("funnel").findOne();
    //const doc = context.services.get("ez-Free-Cluster").db("customerX").collection("funnel").find({});
    const doc = context.services.get("ez-Free-Cluster").db("customerX").collection("funnel").aggregate([{ $sample: { size: 1 } }]).toArray()
      .then(arr => {return arr[0]})
    return  doc;
};
