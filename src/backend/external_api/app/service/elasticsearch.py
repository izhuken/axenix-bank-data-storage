from core.elastic_config import TypeEnum


class ElasticSearchService():
    
    def __init__(self, client):
        self.client = client

    def create_index(self, index_name, properties, index_id):
        result = self.client.index(
            index=index_name,
            document={
                "settings": {"number_of_shards": 2},
                "mappings": {
                    "properties": self.__prepareting_data_index(properties)
                },
            },
            id=index_id,
            ignore=400,
        )
        return result
    
    def insert_data(self, index_name, properties):
        self.client.index(index=index_name,
                        doc_type="_doc",
                        id=properties.get("id_fact"), 
                        document=self.__prepareting_data_insert_update(properties))

    def update_data(self, index_name, properties):
        self.client.index(index=index_name, 
                        id=properties.get("id_fact"), 
                        doc_type="_doc", 
                        document=self.__prepareting_data_insert_update(properties))

    def search(self, index_name, query_param):
        result = self.client.search(index=index_name, body=self.__prepareting_query_for_search(query_param))
        print(result)
        return result


    @staticmethod
    def __prepareting_data_index(data):
        result = {}
    
        for key, value in data.items():
            result[key] = {"type": TypeEnum.__dict__[type(value).__name__.upper()]}

        return result
    
    @staticmethod
    def __prepareting_data_insert_update(data):
        result = {}

        for key, value in data.items():
            result[key] = value
        
        return result
    
    @staticmethod
    def __prepareting_query_for_search(query_param):
        if query_param.get('closed_at_from', False):
            field_name = 'closed_at'
            field_from = query_param['closed_at_from']
            field_to = query_param['closed_at_to']
        
        elif query_param.get('created_at_from', False):
            field_name = 'created_at'
            field_from = query_param['created_at_from']
            field_to = query_param['created_at_to']
        
        if query_param["action_type"] == "avg":
            if query_param.get('credit_sum_from', False):
                field_extension_name = 'credit_sum'
                field_extension_from = query_param['credit_sum_from']
                field_extension_to = query_param['credit_sum_to']
                query = {"query":
                            {"bool":
                                {"must": 
                                    [{"term": 
                                        {"is_closed" : query_param["is_closed"]}
                                    },
                            {"range": 
                                {f"{field_extension_name}": 
                                    {"gte": f"{field_extension_from}", "lte": f"{field_extension_to}"
                                    }
                                }   
                            },
                            ]
                            }
                        },
                        "aggs": 
                            {"range": 
                                {"date_range": 
                                    {"field": f"{field_name}","format": "yyyy-MM-dd", "ranges": 
                                        [{"from": f"{field_from}", "to": f"{field_to}"}]}}, f"{query_param['target_field']}_avg": 
                                            {"avg": 
                                                {"field": f"{query_param['target_field']}"}}}, 
                        "size": 0}
                if query_param.get('contract_number'):
                    field_over_extension_name = 'contract_number'
                    field_over_extension_number = query_param['contract_number']
                    query = query = {"query":
                            {"bool":
                                {"must": 
                                    [{"term": 
                                        {"is_closed" : query_param["is_closed"]}},
                                    {"term":
                                        {f"{field_over_extension_name}": f"{field_over_extension_number}"}
                                    },
                            {"range": 
                                {f"{field_extension_name}": 
                                    {"gte": f"{field_extension_from}", "lte": f"{field_extension_to}"
                                    }
                                }   
                            },
                            ]
                            }
                        },
                        "aggs": 
                            {"range": 
                                {"date_range": 
                                    {"field": f"{field_name}","format": "yyyy-MM-dd", "ranges": 
                                        [{"from": f"{field_from}", "to": f"{field_to}"}]}}, f"{query_param['target_field']}_avg": 
                                            {"avg": 
                                                {"field": f"{query_param['target_field']}"}}}, 
                        "size": 0}
            elif query_param.get('made_payments_from', False):
                field_extension_name = 'made_payments'
                field_extension_from = query_param['made_payments_from']
                field_extension_to = query_param['made_payments_to']
                query = {"query":
                            {"bool":
                                {"must": 
                                    [{"term": 
                                        {"is_closed" : query_param["is_closed"]}
                                    },
                            {"range": 
                                {f"{field_extension_name}": 
                                    {"gte": f"{field_extension_from}", "lte": f"{field_extension_to}"
                                    }
                                }   
                            },
                            ]
                            }
                        },
                        "aggs": 
                            {"range": 
                                {"date_range": 
                                    {"field": f"{field_name}","format": "yyyy-MM-dd", "ranges": 
                                        [{"from": f"{field_from}", "to": f"{field_to}"}]}}, f"{query_param['target_field']}_avg": 
                                            {"avg": 
                                                {"field": f"{query_param['target_field']}"}}}, 
                        "size": 0}
                if query_param.get('contract_number'):
                    field_over_extension_name = 'contract_number'
                    field_over_extension_number = query_param['contract_number']
                    query = query = {"query":
                            {"bool":
                                {"must": 
                                    [{"term": 
                                        {"is_closed" : query_param["is_closed"]}},
                                    {"term":
                                        {f"{field_over_extension_name}": f"{field_over_extension_number}"}
                                    },
                            {"range": 
                                {f"{field_extension_name}": 
                                    {"gte": f"{field_extension_from}", "lte": f"{field_extension_to}"
                                    }
                                }   
                            },
                            ]
                            }
                        },
                        "aggs": 
                            {"range": 
                                {"date_range": 
                                    {"field": f"{field_name}","format": "yyyy-MM-dd", "ranges": 
                                        [{"from": f"{field_from}", "to": f"{field_to}"}]}}, f"{query_param['target_field']}_avg": 
                                            {"avg": 
                                                {"field": f"{query_param['target_field']}"}}}, 
                        "size": 0}
            elif query_param.get('calculated_payment_number_from', False):
                field_extension_name = 'calculated_payment_number'
                field_extension_from = query_param['calculated_payment_number_from']
                field_extension_to = query_param['calculated_payment_number_to']
                query = {"query":
                            {"bool":
                                {"must": 
                                    [{"term": 
                                        {"is_closed" : query_param["is_closed"]}
                                    },
                            {"range": 
                                {f"{field_extension_name}": 
                                    {"gte": f"{field_extension_from}", "lte": f"{field_extension_to}"
                                    }
                                }   
                            },
                            ]
                            }
                        },
                        "aggs": 
                            {"range": 
                                {"date_range": 
                                    {"field": f"{field_name}","format": "yyyy-MM-dd", "ranges": 
                                        [{"from": f"{field_from}", "to": f"{field_to}"}]}}, f"{query_param['target_field']}_avg": 
                                            {"avg": 
                                                {"field": f"{query_param['target_field']}"}}}, 
                        "size": 0}

                if query_param.get('contract_number'):
                    field_over_extension_name = 'contract_number'
                    field_over_extension_number = query_param['contract_number']
                    query = {"query":
                            {"bool":
                                {"must": 
                                    [{"term": 
                                        {"is_closed" : query_param["is_closed"]}},
                                    {"term":
                                        {f"{field_over_extension_name}": f"{field_over_extension_number}"}
                                    },
                            {"range": 
                                {f"{field_extension_name}": 
                                    {"gte": f"{field_extension_from}", "lte": f"{field_extension_to}"
                                    }
                                }   
                            },
                            ]
                            }
                        },
                        "aggs": 
                            {"range": 
                                {"date_range": 
                                    {"field": f"{field_name}","format": "yyyy-MM-dd", "ranges": 
                                        [{"from": f"{field_from}", "to": f"{field_to}"}]}}, f"{query_param['target_field']}_avg": 
                                            {"avg": 
                                                {"field": f"{query_param['target_field']}"}}}, 
                        "size": 0}
            else:
            # query = {"query": {"range" : {f"{field_name}" : {"gte": f"{field_from}", "lte": f"{field_to}"}}, "aggs": {f"{query_param['target_field']}_avg": {"avg": {"field": f"{query_param['target_field']}"}}}}, "size": 0}
                query = {"query": {"term": {"is_closed" : query_param["is_closed"]}}, "aggs": {"range": {"date_range": {"field": f"{field_name}","format": "yyyy-MM-dd", "ranges": [{"from": f"{field_from}", "to": f"{field_to}"}]}}, f"{query_param['target_field']}_avg": {"avg": {"field": f"{query_param['target_field']}"}}}, "size": 0}
            # print(query)
            return query
        
        
        elif query_param["action_type"] == "sum":
            if query_param.get('credit_sum_from', False):
                field_extension_name = 'credit_sum'
                field_extension_from = query_param['credit_sum_from']
                field_extension_to = query_param['credit_sum_to']
                query = {"query":
                            {"bool":
                                {"must": 
                                    [{"term": 
                                        {"is_closed" : query_param["is_closed"]}
                                    },
                            {"range": 
                                {f"{field_extension_name}": 
                                    {"gte": f"{field_extension_from}", "lte": f"{field_extension_to}"
                                    }
                                }   
                            },
                            ]
                            }
                        },
                        "aggs": 
                            {"range": 
                                {"date_range": 
                                    {"field": f"{field_name}","format": "yyyy-MM-dd", "ranges": 
                                        [{"from": f"{field_from}", "to": f"{field_to}"}]}}, f"{query_param['target_field']}_sum": 
                                            {"sum": {"field": f"{query_param['target_field']}"}}}, 
                        "size": 0}
                if query_param.get('contract_number'):
                    field_over_extension_name = 'contract_number'
                    field_over_extension_number = query_param['contract_number']
                    query = {"query":
                            {"bool":
                                {"must": 
                                    [{"term": 
                                        {"is_closed" : query_param["is_closed"]}},
                                    {"term":
                                        {f"{field_over_extension_name}": f"{field_over_extension_number}"}
                                    },
                            {"range": 
                                {f"{field_extension_name}": 
                                    {"gte": f"{field_extension_from}", "lte": f"{field_extension_to}"
                                    }
                                }   
                            },
                            ]
                            }
                        },
                        "aggs": 
                            {"range": 
                                {"date_range": 
                                    {"field": f"{field_name}","format": "yyyy-MM-dd", "ranges": 
                                        [{"from": f"{field_from}", "to": f"{field_to}"}]}}, f"{query_param['target_field']}_sum": 
                                            {"sum": {"field": f"{query_param['target_field']}"}}}, 
                        "size": 0}
            elif query_param.get('made_payments_from', False):
                field_extension_name = 'made_payments'
                field_extension_from = query_param['made_payments_from']
                field_extension_to = query_param['made_payments_to']
                query = {"query":
                            {"bool":
                                {"must": 
                                    [{"term": 
                                        {"is_closed" : query_param["is_closed"]}
                                    },
                            {"range": 
                                {f"{field_extension_name}": 
                                    {"gte": f"{field_extension_from}", "lte": f"{field_extension_to}"
                                    }
                                }   
                            },
                            ]
                            }
                        },
                        "aggs": 
                            {"range": 
                                {"date_range": 
                                    {"field": f"{field_name}","format": "yyyy-MM-dd", "ranges": 
                                        [{"from": f"{field_from}", "to": f"{field_to}"}]}}, f"{query_param['target_field']}_sum": 
                                            {"sum": {"field": f"{query_param['target_field']}"}}}, 
                        "size": 0}
                if query_param.get('contract_number'):
                    field_over_extension_name = 'contract_number'
                    field_over_extension_number = query_param['contract_number']
                    query = {"query":
                            {"bool":
                                {"must": 
                                    [{"term": 
                                        {"is_closed" : query_param["is_closed"]}},
                                    {"term":
                                        {f"{field_over_extension_name}": f"{field_over_extension_number}"}
                                    },
                            {"range": 
                                {f"{field_extension_name}": 
                                    {"gte": f"{field_extension_from}", "lte": f"{field_extension_to}"
                                    }
                                }   
                            },
                            ]
                            }
                        },
                        "aggs": 
                            {"range": 
                                {"date_range": 
                                    {"field": f"{field_name}","format": "yyyy-MM-dd", "ranges": 
                                        [{"from": f"{field_from}", "to": f"{field_to}"}]}}, f"{query_param['target_field']}_sum": 
                                            {"sum": {"field": f"{query_param['target_field']}"}}}, 
                        "size": 0}
            elif query_param.get('calculated_payment_number_from', False):
                field_extension_name = 'calculated_payment_number'
                field_extension_from = query_param['calculated_payment_number_from']
                field_extension_to = query_param['calculated_payment_number_to']
                query = {"query":
                            {"bool":
                                {"must": 
                                    [{"term": 
                                        {"is_closed" : query_param["is_closed"]}
                                    },
                            {"range": 
                                {f"{field_extension_name}": 
                                    {"gte": f"{field_extension_from}", "lte": f"{field_extension_to}"
                                    }
                                }   
                            },
                            ]
                            }
                        },
                        "aggs": 
                            {"range": 
                                {"date_range": 
                                    {"field": f"{field_name}","format": "yyyy-MM-dd", "ranges": 
                                        [{"from": f"{field_from}", "to": f"{field_to}"}]}}, f"{query_param['target_field']}_sum": 
                                            {"sum": {"field": f"{query_param['target_field']}"}}}, 
                        "size": 0}

                if query_param.get('contract_number'):
                    field_over_extension_name = 'contract_number'
                    field_over_extension_number = query_param['contract_number']
                    query = {"query":
                            {"bool":
                                {"must": 
                                    [{"term": 
                                        {"is_closed" : query_param["is_closed"]}},
                                    {"term":
                                        {f"{field_over_extension_name}": f"{field_over_extension_number}"}
                                    },
                            {"range": 
                                {f"{field_extension_name}": 
                                    {"gte": f"{field_extension_from}", "lte": f"{field_extension_to}"
                                    }
                                }   
                            },
                            ]
                            }
                        },
                        "aggs": 
                            {"range": 
                                {"date_range": 
                                    {"field": f"{field_name}","format": "yyyy-MM-dd", "ranges": 
                                        [{"from": f"{field_from}", "to": f"{field_to}"}]}}, f"{query_param['target_field']}_sum": 
                                            {"sum": {"field": f"{query_param['target_field']}"}}}, 
                        "size": 0}
            else:
                query = {"query": {"term": {"is_closed" : query_param["is_closed"]}}, "aggs": {"range": {"date_range": {"field": f"{field_name}","format": "yyyy-MM-dd", "ranges": [{"from": f"{field_from}", "to": f"{field_to}"}]}}, f"{query_param['target_field']}_sum": {"sum": {"field": f"{query_param['target_field']}"}}}, "size": 0}
            return query
        

        elif query_param["action_type"] == "count":
            if query_param.get('credit_sum_from', False):
                field_extension_name = 'credit_sum'
                field_extension_from = query_param['credit_sum_from']
                field_extension_to = query_param['credit_sum_to']
                query = {"query":
                            {"bool":
                                {"must": 
                                    [{"term": 
                                        {"is_closed" : query_param["is_closed"]}
                                    },
                            {"range": 
                                {f"{field_extension_name}": 
                                    {"gte": f"{field_extension_from}", "lte": f"{field_extension_to}"
                                    }
                                }   
                            },
                            ]
                            }
                        },
                        "aggs": 
                            {"range": 
                                {"date_range": 
                                    {"field": f"{field_name}","format": "yyyy-MM-dd", "ranges": 
                                        [{"from": f"{field_from}", "to": f"{field_to}"}]}}, f"{query_param['target_field']}_count": 
                                            {"value_count": {"field": f"{query_param['target_field']}"}}}, 
                        "size": 0}
                if query_param.get('contract_number'):
                    field_over_extension_name = 'contract_number'
                    field_over_extension_number = query_param['contract_number']
                    query = {"query":
                            {"bool":
                                {"must": 
                                    [{"term": 
                                        {"is_closed" : query_param["is_closed"]}},
                                    {"term":
                                        {f"{field_over_extension_name}": f"{field_over_extension_number}"}
                                    },
                            {"range": 
                                {f"{field_extension_name}": 
                                    {"gte": f"{field_extension_from}", "lte": f"{field_extension_to}"
                                    }
                                }   
                            },
                            ]
                            }
                        },
                        "aggs": 
                            {"range": 
                                {"date_range": 
                                    {"field": f"{field_name}","format": "yyyy-MM-dd", "ranges": 
                                        [{"from": f"{field_from}", "to": f"{field_to}"}]}}, f"{query_param['target_field']}_count": 
                                            {"value_count": {"field": f"{query_param['target_field']}"}}}, 
                        "size": 0}
            elif query_param.get('made_payments_from', False):
                field_extension_name = 'made_payments'
                field_extension_from = query_param['made_payments_from']
                field_extension_to = query_param['made_payments_to']
                query = {"query":
                            {"bool":
                                {"must": 
                                    [{"term": 
                                        {"is_closed" : query_param["is_closed"]}
                                    },
                            {"range": 
                                {f"{field_extension_name}": 
                                    {"gte": f"{field_extension_from}", "lte": f"{field_extension_to}"
                                    }
                                }   
                            },
                            ]
                            }
                        },
                        "aggs": 
                            {"range": 
                                {"date_range": 
                                    {"field": f"{field_name}","format": "yyyy-MM-dd", "ranges": 
                                        [{"from": f"{field_from}", "to": f"{field_to}"}]}}, f"{query_param['target_field']}_count": 
                                            {"value_count": {"field": f"{query_param['target_field']}"}}}, 
                        "size": 0}
                if query_param.get('contract_number'):
                    field_over_extension_name = 'contract_number'
                    field_over_extension_number = query_param['contract_number']
                    query = {"query":
                            {"bool":
                                {"must": 
                                    [{"term": 
                                        {"is_closed" : query_param["is_closed"]}},
                                    {"term":
                                        {f"{field_over_extension_name}": f"{field_over_extension_number}"}
                                    },
                            {"range": 
                                {f"{field_extension_name}": 
                                    {"gte": f"{field_extension_from}", "lte": f"{field_extension_to}"
                                    }
                                }   
                            },
                            ]
                            }
                        },
                        "aggs": 
                            {"range": 
                                {"date_range": 
                                    {"field": f"{field_name}","format": "yyyy-MM-dd", "ranges": 
                                        [{"from": f"{field_from}", "to": f"{field_to}"}]}}, f"{query_param['target_field']}_count": 
                                            {"value_count": {"field": f"{query_param['target_field']}"}}}, 
                        "size": 0}
            elif query_param.get('calculated_payment_number_from', False):
                field_extension_name = 'calculated_payment_number'
                field_extension_from = query_param['calculated_payment_number_from']
                field_extension_to = query_param['calculated_payment_number_to']
                query = {"query":
                            {"bool":
                                {"must": 
                                    [{"term": 
                                        {"is_closed" : query_param["is_closed"]}
                                    },
                            {"range": 
                                {f"{field_extension_name}": 
                                    {"gte": f"{field_extension_from}", "lte": f"{field_extension_to}"
                                    }
                                }   
                            },
                            ]
                            }
                        },
                        "aggs": 
                            {"range": 
                                {"date_range": 
                                    {"field": f"{field_name}","format": "yyyy-MM-dd", "ranges": 
                                        [{"from": f"{field_from}", "to": f"{field_to}"}]}}, f"{query_param['target_field']}_count": 
                                            {"value_count": {"field": f"{query_param['target_field']}"}}}, 
                        "size": 0}

                if query_param.get('contract_number'):
                    field_over_extension_name = 'contract_number'
                    field_over_extension_number = query_param['contract_number']
                    query = {"query":
                            {"bool":
                                {"must": 
                                    [{"term": 
                                        {"is_closed" : query_param["is_closed"]}},
                                    {"term":
                                        {f"{field_over_extension_name}": f"{field_over_extension_number}"}
                                    },
                            {"range": 
                                {f"{field_extension_name}": 
                                    {"gte": f"{field_extension_from}", "lte": f"{field_extension_to}"
                                    }
                                }   
                            },
                            ]
                            }
                        },
                        "aggs": 
                            {"range": 
                                {"date_range": 
                                    {"field": f"{field_name}","format": "yyyy-MM-dd", "ranges": 
                                        [{"from": f"{field_from}", "to": f"{field_to}"}]}}, f"{query_param['target_field']}_count": 
                                            {"value_count": {"field": f"{query_param['target_field']}"}}}, 
                        "size": 0}
            else:
                query = {"query": {"term": {"is_closed" : query_param["is_closed"]}}, "aggs": {"range": {"date_range": {"field": f"{field_name}","format": "yyyy-MM-dd", "ranges": [{"from": f"{field_from}", "to": f"{field_to}"}]}}, f"{query_param['target_field']}_count": {"value_count": {"field": f"{query_param['target_field']}"}}}, "size": 0}
            return query
# print(_es.search(index="penis", body=json.dumps({"query":{"match": {"id_fact" : str(uuid_field)}}})))

# credit_sum_from: float | None = Field(default=None)
# credit_sum_to: float | None = Field(default=None)
# made_payments_from: float | None = Field(default=None)
# made_payments_to: float | None = Field(default=None)
# payment_number_from: int | None = Field(default=None)
# payment_number_to: int | None = Field(default=None)
# calculated_payment_number_from: int | None = Field(default=None)
# calculated_payment_number_to: int | None = Field(default=None)
# is_closed: bool
# closed_at_from: date | None = Field(default=None)
# closed_at_to: date | None = Field(default=None)
# contract_number: int | None = Field(default=None)
# create_at_from: date | None = Field(default=None)
# create_at_to: date | None = Field(default=None)
# action_type: str
# target_field: str