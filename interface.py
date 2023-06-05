# import os
#
# if os.getenv("ENV", "dev") == "dev":
#     origins = [
#         f"http://localhost:8000",
#         "https://chat.openai.com",
#     ]
#
#     app.add_middleware(
#         CORSMiddleware,
#         allow_origins=origins,
#         allow_credentials=True,
#         allow_methods=["*"],
#         allow_headers=["*"],
#     )