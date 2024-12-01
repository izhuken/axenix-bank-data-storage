
from typing import Annotated

from app.schemas.fact_search_schemas import SearchRequest, SearchResponse
from app.service.elasticsearch import ElasticSearchService
from core.elastic_config import _es
from fastapi import APIRouter, Query

search_router = APIRouter(tags=["SearchRouter"])
elastic_service = ElasticSearchService(_es)
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
@search_router.get('/search', response_model=SearchResponse)
async def search(data: Annotated[SearchRequest, Query()]) -> SearchResponse | None:
    result = elastic_service.search("fact", {**data.dict(exclude_none=True)})

    if result.get("aggregations").get(f"{data.target_field}_{data.action_type}").get("value") == None:
        return SearchResponse(target_value=0)

    return SearchResponse(target_value=round(result.get("aggregations").get(f"{data.target_field}_{data.action_type}").get("value"), 2))