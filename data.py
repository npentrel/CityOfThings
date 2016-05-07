new_customer = {
          "name": "DisplayName",
            "status": "Active",
              "description": "Description string",
                "validFor": {
                        "startDateTime": "2013-06-19T04:00:00.0Z",
                            "endDateTime": "2013-04-19T20:42:23.0Z"
                              },
                  "customerRank": "3",
                    "relatedParty": {
                            "id": "1",
                                "href": "http://serverlocation:port/partyManagement/individual/1",
                                    "role": "customer",
                                        "name": "John Doe"
                                          },
                      "characteristic": [
                              {
                                        "name": "characteristicname1",
                                              "value": "characteristicvalue1"
                                                  },
                                  {
                                            "name": "characteristicname2",
                                                  "value": "characteristicvalue2"
                                                      }
                                    ],
                        "contactMedium": [
                                {
                                          "type": "Email",
                                                "validFor": {
                                                            "startDateTime": "2013-04-19T20:42:23.0Z"
                                                                  },
                                                      "medium": {
                                                                  "emailAddress": "abc@tmforum.com"
                                                                        }
                                                          },
                                            {
                                                      "preferred": True,
                                                            "type": "TelephoneNumber",
                                                                  "validFor": {
                                                                              "startDateTime": "2013-04-19T20:42:23.0Z"
                                                                                    },
                                                                        "medium": {
                                                                                    "type": "business",
                                                                                            "number": "+436641234567"
                                                                                                  }
                                                                            }
                                              ],
                          "customerAccount": [
                                      {
                                                "id" : "1",
                                                      "href": "http://serverlocation:port/customerManagement/customerAccount/1",
                                                            "name": "CustomerAccount1",
                                                                  "description": "CustomerAccountDesc1",
                                                                        "status": "Active"
                                                                            },
                                          {
                                                    "id" :"2",
                                                          "href": "http://serverlocation:port/customerManagement/customerAccount/2",
                                                                "name": "CustomerAccount2",
                                                                      "description": "CustomerAccountDesc2",
                                                                            "status": "Active"
                                                                                }
                                            ],
                            "customerCreditProfile": [
                                        {
                                                  "creditProfileDate": "2013-04-19T20:42:23.0Z",
                                                        "validFor": {
                                                                    "startDateTime": "2013-04-19T20:42:23.0Z",
                                                                            "endDateTime": "2013-06-19T04:00:00.0Z"
                                                                                  },
                                                              "creditRiskRating": 1,
                                                                    "creditScore": 1
                                                                        },
                                            {
                                                      "creditProfileDate": "2013-04-19T20:42:23.0Z",
                                                            "validFor": {
                                                                        "startDateTime": "2013-04-19T20:42:23.0Z",
                                                                                "endDateTime": "2013-06-19T04:00:00.0Z"
                                                                                      },
                                                                  "creditRiskRating": 1,
                                                                        "creditScore": 1
                                                                            }
                                              ],
                              "paymentMean": [
                                          {
                                                    "id" : "45",
                                                          "href": "http://serverlocation:port/customerManagement/paymentMean/45",
                                                                "name": "my favourite payment mean"
                                                                    },
                                              {
                                                        "id" : "64",
                                                              "href": "http://serverlocation:port/customerManagement/paymentMean/64",
                                                                    "name": "my credit card payment mean"
                                                                        }
                                                ]
                              }
