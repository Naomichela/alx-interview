#!/usr/bin/node

// Import the request module
const request = require('request');

// Get the movie ID from the command-line arguments
const movieId = process.argv[2];

// Base URL for the Star Wars API
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

// Make a request to the Star Wars API for the specified movie
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Parse the response body to get JSON data
  const data = JSON.parse(body);

  // Retrieve the character URLs array from the data
  const characters = data.characters;

  // Function to fetch each character's name and print it
  const printCharacterName = (url) => {
    request(url, (err, res, characterBody) => {
      if (err) {
        console.error(err);
        return;
      }
      const characterData = JSON.parse(characterBody);
      console.log(characterData.name);
    });
  };

  // Iterate through the character URLs and print each name
  characters.forEach((characterUrl) => printCharacterName(characterUrl));
});

