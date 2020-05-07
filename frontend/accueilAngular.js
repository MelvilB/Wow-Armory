var app = angular.module("Accueil", []);

//définir les variables qui seront utilisés dans la 2eme partie (vides à l'origine)
var dict = new Map();

app.controller("globalController", function($scope){
	$scope.pseudo="";
	$scope.faction="";
	$scope.background={};
	$scope.accueil = true;
	$scope.armory = false;
	$scope.answer = "";
	$scope.itemId = new Array(19);
	//$scope.itemId = [-1,-1,-1,135029,132624,132495,134583,132535,132602,132938,-1,-1,-1,-1,133754,135350,-1,-1,-1];

	$scope.get = async function(faction){
		if($scope.pseudo.length >= 2 && $scope.pseudo.length <= 12){
			$scope.faction = faction;
			var request = new XMLHttpRequest();
			var verif = false;
			request.onreadystatechange = function() {
				if (this.readyState == XMLHttpRequest.DONE && this.status == 200) {
			        var response = JSON.parse(this.responseText);
			        console.log(response);
			        $scope.itemId = response["currently_equipped"];
			        for(var i=0; i<19; i++){
			        	//$scope.itemId[i]=parseInt($scope.itemId[i], 10)
			        	/*if($scope.itemId[i]=="-1"){
			        		$scope.itemId[i]="132602";
			        	}*/
			        	$scope.itemId[i] = "https://fr.wowhead.com/item="+$scope.itemId[i];
			        }
			        console.log($scope.itemId);
			        verif = true;
			    }	
				
			};
			
			request.open("GET", "https://mysterious-lake-46753.herokuapp.com/data/?pseudo=" + $scope.pseudo + "&faction=" + $scope.faction);
			request.send();
			while(verif==false){
				await sleep(20);
			}
			console.log($scope.itemId);


			console.log("test");
			/*$scope.background={"background" : "url(images/" + faction +".jpg) no-repeat center center fixed "};
			$scope.accueil = false;
			$scope.armory = true;
			if(faction=="Alliance"){
				document.getElementById('characterName').style.color="#68CCEF";
			} else {
				document.getElementById('characterName').style.color="#C41E3B";
			}*/

			/*
			var request2 = new XMLHttpRequest();
			request2.onreadystatechange = function() {
			    if (this.readyState == XMLHttpRequest.DONE && this.status == 200) {
			        var response = JSON.parse(this.responseText);
			        console.log(response.current_condition.condition);
			    }
			};
			request2.open("GET", "https://fr.wowhead.com/icon=133968");
			//request2.withCredentials = true;
			request2.setHeader("Access-Control-Allow-Origin", "*");
			//request2.setRequestHeader("Access-Control-Allow-Methods", "*");
			//request2.setRequestHeader("Allow", "*");
			//request.open("GET", "https://wow.zamimg.com/images/wow/icons/large/inv_misc_food_12.jpg");
			request2.send();*/

			$scope.accueil = false;
			$scope.armory = true;
			if(faction=="Alliance"){
				document.getElementById('characterName').style.color="#68CCEF";
			} else {
				document.getElementById('characterName').style.color="#C41E3B";
			}
			$scope.background={"background" : "url(images/" + faction +".jpg) no-repeat center center fixed "};

			console.log("scope.accueil: "+$scope.accueil);
			console.log("scope.armory: "+$scope.armory);
			console.log("scope.background: "+$scope.background);
		}
	};

	$scope.back = function(){
		$scope.armory = false;
		$scope.accueil= true;
		$scope.background={"background" : "url(images/accueil.png) no-repeat center center fixed "};
	};
});

app.controller("itemController", function($scope){
	$scope.inside=false;
	//$scope.infoItem={"B1":"ceci sont les caractéristiques de l'item B1"; "B2":"ceci sont les caractéristiques de l'item B2"}
	$scope.infoShow="";
	$scope.test="";
	$scope.getShow=function(numItem){
		if(numItem=="none"){
			$scope.inside=false;
		}else{
			$scope.inside=true;
		}
		var position = getPosition(numItem);
		const element = document.getElementById('info');
		element.style.position = "absolute";
		element.style.top = position[1] + 30 +'px';
		element.style.left = position[0] + 100 +'px';

		//$scope.infoShow=$scope.infoItem[numItem];
	};
});


/*
const page = document.body;
//const page = document.getElementsByClassName("item");
const mousex = document.getElementById('mouse-x')
const mousey = document.getElementById('mouse-y')
page.addEventListener('mousemove', function(event) {
    //var x = event.offsetX;
	//var y = event.offsetY;
	var x = event.pageX;
	var y = event.pageY;
	//var scrollY = document.body.scrollTop || document.documentElement.scrollTop;
	//var scrollX = document.body.scrollLeft || document.documentElement.scrollLeft;
	var element = document.getElementById('info');
	//element.style.left = x + scrollX +'px';
	//element.style.top = y + scrollY +'px';
	element.style.position = "absolute";
	element.style.left = x +'px';
	element.style.top = y +'px';
	mousex.innerHTML = event.pageX; 
    mousey.innerHTML = event.pageY; 
});
*/


function getPosition(element)
{
	var left = 0;
	var top = 0;
	/*On récupère l'élément*/
	var e = document.getElementById("item"+element);
	/*Tant que l'on a un élément parent*/
	while (e.offsetParent != undefined && e.offsetParent != null)
	{
		/*On ajoute la position de l'élément parent*/
		left += e.offsetLeft + (e.clientLeft != null ? e.clientLeft : 0);
		top += e.offsetTop + (e.clientTop != null ? e.clientTop : 0);
		e = e.offsetParent;
	}
	return new Array(left,top);
};


function readData(){
	const MongoClient = require('mongodb').MongoClient;
	const url = 'mongodb+srv://dbUser2:dbUser2@cluster0-ll4tc.mongodb.net/test?retryWrites=true&w=majority';
	const assert = require('assert');

	var list = MongoClient.connect(url, {useUnifiedTopology: true}, async function(err, client) {
		assert.equal(null, err);
		const collection = await client.db("wow_test").collection("icons");
		var cursor = await collection.find({name: "Banzai"});
		var test = await cursor.toArray();
		var list = test[0];
	 	client.close();
	 	return list;
	});
	return list;
};

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}