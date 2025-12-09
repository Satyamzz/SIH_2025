from fastapi import FastAPI
from analytics_services.admin_side.get_companies import router as company_router
from analytics_services.admin_side.get_batch import router as year_router
from analytics_services.admin_side.to_not_be_used.filter_skills import router as skills_filter_router
from analytics_services.admin_side.to_not_be_used.filter_year import router as graduation_year_filter_route
from analytics_services.admin_side.to_not_be_used.filter_job_location import router as job_location_filter_route
from analytics_services.admin_side.skill_stats import router as skill_stats_route
from analytics_services.admin_side.get_locations import router as location_router
from analytics_services.admin_side.to_not_be_used.filter_companies import router as filter_company_router
from analytics_services.admin_side.get_branch_distribution import router as batch_dist
from analytics_services.admin_side.summarize import router as summary
from recommendation_system.skill_rec_emb import router as skill_recommendation
from ner_model.ner_main import router as skill_extract
from analytics_services.admin_side.to_not_be_used.check_verification import router as cv
from analytics_services.admin_side.total_verified import router as tv
from analytics_services.admin_side.completion_stats import router as completion_stats
from recommendation_system.alumni_network import router as alum_rec
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
app.include_router(summary)
app.include_router(skill_recommendation)
app.include_router(skill_extract)
app.include_router(cv)
app.include_router(tv)
app.include_router(completion_stats)
app.include_router(alum_rec)