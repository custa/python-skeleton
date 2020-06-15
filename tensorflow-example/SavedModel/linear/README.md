
对输入张量的维度似乎没有太多限制

```
curl http://localhost:18501/v1/models/linear/metadata
```
```
{
"model_spec":{
 "name": "linear",
 "signature_name": "",
 "version": "1573026833"
}
,
"metadata": {"signature_def": {
 "signature_def": {
  "serving_default": {
   "inputs": {
    "x": {
     "dtype": "DT_FLOAT",
     "tensor_shape": {
      "dim": [
       {
        "size": "-1",
        "name": ""
       },
       {
        "size": "1",
        "name": ""
       }
      ],
      "unknown_rank": false
     },
     "name": "Input-X:0"
    }
   },
   "outputs": {
    "y": {
     "dtype": "DT_FLOAT",
     "tensor_shape": {
      "dim": [
       {
        "size": "-1",
        "name": ""
       },
       {
        "size": "1",
        "name": ""
       }
      ],
      "unknown_rank": false
     },
     "name": "Output-Y:0"
    }
   },
   "method_name": "tensorflow/serving/predict"
  }
 }
}
}
}
```
```
curl -d '{"instances": [[1, 2, 3], [4, 5, 6], [7, 8, 9]] }' http://localhost:18501/v1/models/linear:predict
```
```
{
    "predictions": [[2.5, 3.0, 3.5], [4.0, 4.5, 5.0], [5.5, 6.0, 6.5]
    ]
}
```
