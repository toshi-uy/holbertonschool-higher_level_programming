$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  const films = data.results;
  films.forEach(element => {
    $('UL#list_movies').append('<li>' + element.title + '</li>');
  });
});
