function search() {
	var input, tr, td, title;
	input = document.getElementById("input").value.toUpperCase();
	tr = document.getElementsByClassName("a");
	title = document.getElementsByClassName("b");

		for (var i = 0; i < tr.length; i++) {
			tr[i].style.backgroundColor = "";
			tr[i].style.border = "";
			title[i].style.backgroundColor = "";
			title[i].style.border = "";
		}

		if (input !== "") {
			for (var i = 0; i < tr.length; i++) {
			td = tr[i].getElementsByTagName("td")[0];
				if (td) {
					if (td.innerHTML.toUpperCase().indexOf(input) > -1) {
						tr[i].style.backgroundColor = "#05A823";
						tr[i].style.border = "medium solid #047A19";
						title[i].style.backgroundColor = "#05A823";
						title[i].style.border = "medium solid #047A19";
					}
				}
			}
		}
		
}


function filter() {
	var genre, genresel, tr, td, title;

	genre = document.getElementById("select");
	genresel = genre.options[genre.selectedIndex].text;
	tr = document.getElementsByClassName("a");
	title = document.getElementsByClassName("b");

	if (genresel !== "Genre") {
		for (var i = 0; i < tr.length; i++) {
		    td = tr[i].getElementsByTagName("td")[2];
		    if (td) {
		      if (td.innerHTML.indexOf(genresel) > -1) {
		        tr[i].style.display = "";
		        title[i].style.display = "";
		      } else {
		        tr[i].style.display = "none";
		        title[i].style.display = "none";
		      }
		    } 
		}
	} else {
		for (var i = 0; i < tr.length; i++) {
			tr[i].style.display = "";
			title[i].style.display = "";
		}
	}
	
}

function makeLeaderboard() {
	var titleLeaderboard, description, genre, author;

	titleLeaderboard = document.getElementById('titleLeaderboard');
	description = document.getElementById('description');
	genre = document.getElementById('genre');
	author = document.getElementById('author');

	$('#submit').click(function() {
		var formdata = serialize();
		$.ajax({
					type: 'POST',
				 contentType: 'application/json',
				 data: JSON.stringify(formdata),
				 dataType: 'json',
				 url: 'http://192.168.57.223:5000/createform',
				 success: function (e) {
						 console.log(e);
						 window.location = "http://192.168.57.223:5000/preview";
				 },
				 error: function(error) {
				 console.log(error);
		 }
		 });
 });

	// $.ajax({
	// 	type: "POST",
	// 	url: "../main.py",
	// 	data: { 'titleLeaderboard': titleLeaderboard, 'description': description, 'genre': genre, 'author': author}
	// }).done(function( o ) {
	// 	 console.log(data)
	// });
}