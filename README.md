# How does it work? 
-------------------

Smart city improvement game - do good, get points, collect rewards!

<<<<<<< 5e5030eed8bbf19de680e2bb900e8dd863e1d078
##How does it work? 
=======
>>>>>>> Added API enpoint documentation
* Build with Python Flask on IBM BlueMix
* Android for the frontend

##Integrated APIs
- [ ] TM Forum APIs
    - [ ] Trouble Ticket 
    - [ ] Customer Management 
    - [ ] Product Catalog Management
    - [ ] Product Inventory Management
    - [ ] Product Ordering
    - [ ] Billing Management
    - [ ] Party Management
    - [ ] SLA Management
    - [ ] Usage Management
    - [ ] Performance Management
- [x] IBM BlueMix
- [ ] Ericsson APIs
- [ ] IWARE APIs
- [ ] AirSensa Data API
- [ ] Nice Open Data

<<<<<<< 5e5030eed8bbf19de680e2bb900e8dd863e1d078
=======

>>>>>>> Added API enpoint documentation
# User

## Create User

Creates new user in the game

`PUSH /api/user'

### Parameters

| Name      | Type   | Description              |
|-----------|--------|--------------------------|
| FirstName | String |                          |
| LastName  | String |                          |
| Email     | String |                          |
| Interests | List   | String list of interests |

### Response

```
    HTTP/1.1 200 OK
    {
        "userid": 31337
    }
```

### Error Response

```
HTTP/1.1 400 Bad Request
```

# Tasks

## Get Tasks

Gets all the tasks from a user

`GET /api/tasks`

### Parameters

| Name   | Type | Description |
|--------|------|-------------|
| Userid | int  |             |

### Response

``` 
    HTTP/1.1 200 OK
    { 
        "tasks":
            [
                {
                    "title": "Clean the road"
                    "content": "Lorem ipsum wololo ipsum"
                    "coordinates": [1.0, 2.0]
                    "address": "Rue de Wololo"
                    "category": "cleanup"
                    "time": "2012-04-23T18:25:43.511Z"
                    "id": 420
                },
            ]
    }
```

### Error Response

```
HTTP/1.1 400 Bad Request
```

## Sign up

`PUSH api/tasks/signup`

### Parameters

| Name   | Type | Description |
|--------|------|-------------|
| taskID | int  |             |


# Rewards 

## Get rewards 

Gets all the rewards available

`GET /api/rewards'

### Parameters

| Name   | Type | Description |
|--------|------|-------------|
| Userid | int  |             |

### Response

```
    HTTP/1.1 200 OK
    {
        "Rewards": 
            [
                {
                    "title": "Amazon $100 voucher"
                    "content":
                    "points": 100
                    "id" : 1337
                },
            ]
    }
```

### Error Response

```
HTTP/1.1 400 Bad Request
```

## Redeem rewards 

Gets all the rewards available

`GET /api/rewards/(id: int)'


### Response

```
    HTTP/1.1 200 OK
```

### Error Response

```
    HTTP/1.1 400 Bad Request
    {
        "error": "insuficientFunds"
    }
```

