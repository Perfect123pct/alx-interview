#!/usr/bin/node

const request = require('request');

// Extract movie ID from command line arguments
const movieId = process.argv[2];

// URL of the Star Wars API endpoint for films
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

// Make a GET request to the API endpoint
request(apiUrl, function(error, response, body) {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Status:', response.statusCode);
  } else {
    // Parse JSON response
    const filmData = JSON.parse(body);

    // Extract character URLs from film data
    const characterURLs = filmData.characters;

    // Make parallel requests to fetch character data
    Promise.all(
      characterURLs.map(url =>
        new Promise((resolve, reject) => {
          request(url, (error, response, body) => {
            if (error) {
              reject(error);
            } else if (response.statusCode !== 200) {
              reject(`Failed to fetch ${url}: Status ${response.statusCode}`);
            } else {
              const characterData = JSON.parse(body);
              resolve(characterData.name);
            }
          });
        })
      )
    )
    .then(characterNames => {
      // Print character names
      characterNames.forEach(name => console.log(name));
    })
    .catch(error => {
      console.error('Error fetching character data:', error);
    });
  }
});

