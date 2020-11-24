# sojern-questions

## Prerequisites

- Python (3+)
- Flask

Please have Python 3 and Flask installed before running the code.
Flask can be installed using pip.

## Getting stated

git clone https://github.com/DMevada/sojern-questions
cd sojern-questions

## Math API

To run the math_api.py, execute the command below

```
python math_api.py
```

This will start a webserver on the default port of 5000.
Using a REST client, make requests to the following APIs.
All APIs are using a POST method because JSON data is expected, and it is
cumbersome to send multiple values with GET.

- /min
- /max
- /avg
- /median
- /percentile

### Expected Body

/min
```
{
	"values": [4,8,2,1,7,12,22,-9],
	"quantifier": 1
}
```

/max
```
{
	"values": [4,8,2,1,7,12,22,-9],
	"quantifier": 5
}
```

/avg
```
{
	"values": [4,8,2,1,7,12,22,-9],
	"quantifier": 5
}
```

/median
```
{
	"values": [10,12,6,9,8,14]
}
```

/percentile
```
{
	"values": [10,12,6,9,8,14],
	"quantifier": "50"
}
```

### Success Response

/min
```
{
  "minimum": [
    -9
  ],
  "status": "success"
}
```

/max
```
{
  "maximum": [
    22,
    12,
    8,
    7,
    4
  ],
  "status": "success"
}
```

/avg
```
{
  "average": 5.875,
  "status": "success"
}
```

/median
```
{
  "median": 9.5,
  "status": "success"
}
```

/percentile
```
{
  "percentile": 9,
  "status": "success"
}
```

### Error Response

Error response is sent if required keys are missing from the request JSON data.

Missing values key
```
{
  "message": "values key containing a list of numbers must be present in JSON body",
  "status": "error"
}
```

Missing quantifier key
```
{
  "message": "quantifier key containing a list of numbers must be present in JSON body",
  "status": "error"
}
```

## Version Compare

This script compares two versions containing "." and integers.
The versions should contain atleast one "." and should be properly formatted.

To run the version compare, execute the command below

```
python compare_version.py
```

### Valid versions

```
a.b
a.b.c
a.b.c.d

etc.
```

### Invalid versions

```
.a
a.
a.b.
.a.b.
```

There should be no leading or lagging ".".
The separators should be surrounded by numbers.
In the examples above, a,b,c,d are placeholders for integers.
If the input is not an integer, parsing will be incorrect.
