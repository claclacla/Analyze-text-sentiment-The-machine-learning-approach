# Analyze text sentiment:The machine learning approach

This project is based on Andrew Trask "Sentiment network" exercise.
The dataset is part of the "Learning Word Vectors for Sentiment Analysis" publication.

--------------------------------------------------------------------------------

### Prerequisites

What things you need to install the software

```
docker 17+
docker-compose 1.19.0+

```

--------------------------------------------------------------------------------

### Installing

```
# Change the directory to the project folder
cd path-to-your-project-folder

# Create a .env file with your local project folder
echo "APP_FOLDER=/path-to-your-project-folder" > .env

# Build the project environment
sudo docker-compose -f docker/docker-compose.yaml build

```

--------------------------------------------------------------------------------

### Executing

```
# Run the project environment
sudo docker-compose -f docker/docker-compose.yaml up -d

# Execute the jupyter notebook server 
sudo docker exec -it JupiterNotebook jupyter notebook --notebook-dir=/usr/src/app/notebooks --ip='*' --port=8888 --no-browser --allow-root 

```

--------------------------------------------------------------------------------

## Authors

- **Simone Adelchino** - [github](https://github.com/claclacla)

--------------------------------------------------------------------------------

## Acknowledgments

- **Andrew Trask blog** - [github](http://iamtrask.github.io/)
- **Sentiment network project** - [github](https://github.com/udacity/deep-learning/tree/master/sentiment-network)
- **Learning Word Vectors for Sentiment Analysis** - [Large Movie Review Dataset v1.0](http://ai.stanford.edu/~amaas/data/sentiment/)
