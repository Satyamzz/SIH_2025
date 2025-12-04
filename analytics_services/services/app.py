from fastapi import FastAPI
from get_companies import router as company_router
from get_batch import router as year_router
from filter_skills import router as skills_filter_router
from filter_year import router as graduation_year_filter_route
from filter_job_location import router as job_location_filter_route
from skill_stats import router as skill_stats_route
from get_locations import router as location_router
from filter_companies import router as filter_company_router
from get_branch_distribution import router as batch_dist
app = FastAPI()

# include the router
app.include_router(company_router)
app.include_router(year_router)
app.include_router(skills_filter_router)
app.include_router(graduation_year_filter_route)
app.include_router(job_location_filter_route)
app.include_router(skill_stats_route)
app.include_router(location_router)
app.include_router(filter_company_router)
app.include_router(batch_dist)
