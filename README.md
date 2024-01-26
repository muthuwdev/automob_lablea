# automob_lablea

# Initial setup for the django project with postgres database integrated.

To build the images and to run the containers in background please run bellow commands.
    docker compose -f local.yml config
    docker compose -f local.yml up --build -d --remove-orphans

Then two containers will start to run 
    1. The django api container
    2. The postgres container

