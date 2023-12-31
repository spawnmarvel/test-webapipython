import logging

import azure.functions as func

# updated yamls file
# Test github settings->Actions->Allow spawnmarvel actions and reusable workflows
# Failed

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully with a parameter 2.")
    else:
        return func.HttpResponse(
             "Github Actions 1.1: This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )


