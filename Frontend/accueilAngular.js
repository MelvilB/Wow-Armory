var app = angular.module("Accueil", []);

app.controller("globalController", function($scope){
	$scope.pseudo="";
	$scope.faction="";
	$scope.race="";
	$scope.gender="";
	$scope.background={};
	$scope.accueil = true;
	$scope.armory = false;
	$scope.dataPlayer = new Map();
	$scope.itemId = new Array(19);
	$scope.itemPath = new Array(19);
	$scope.loader=false;
	$scope.error=false;
	//$scope.itemId = [-1,-1,-1,135029,132624,132495,134583,132535,132602,132938,-1,-1,-1,-1,133754,135350,-1,-1,-1];

	$scope.get = async function(faction){
		if($scope.pseudo.length >= 2 && $scope.pseudo.length <= 12){
			if($scope.race==""){
				$scope.error=true;
				$scope.back();
			} else {
				//console.log($scope.faction);
				$scope.faction = faction;
				$scope.loader = true;
				$scope.$apply();
				//console.log($scope.faction);

				var request = new XMLHttpRequest();
				var verif = false;
				request.onreadystatechange = function() {
					if (this.readyState == XMLHttpRequest.DONE && this.status == 200) {
				        var response = JSON.parse(this.responseText);
				        //console.log(response);
				        $scope.dataPlayer=response;
				        
				        if($scope.dataPlayer['name']=="introuvable"){
				        	$scope.loader = false;
				        	$scope.error=true;
				        	$scope.back();
				        } else {

				        	$scope.accueil = false;
							$scope.armory = true;
							if($scope.faction=="Alliance"){
								document.getElementById('characterName').style.color = "#68CCEF";
							} else {
								document.getElementById('characterName').style.color = "#C41E3B";
							}
							$scope.background={"background" : "url(images/" + faction + ".jpg) no-repeat center center fixed"};

					        $scope.itemId = response["currently_equipped"];
					        $scope.itemPath[0] = response["url_list"][0];
					        $scope.itemPath[1] = response["url_list"][1];
					        $scope.itemPath[2] = response["url_list"][2];
					        $scope.itemPath[3] = response["url_list"][14];
					        $scope.itemPath[4] = response["url_list"][4];
					        $scope.itemPath[5] = response["url_list"][3];
					        $scope.itemPath[6] = response["url_list"][18];
					        $scope.itemPath[7] = response["url_list"][8];
					        $scope.itemPath[8] = response["url_list"][9];
					        $scope.itemPath[9] = response["url_list"][5];
					        $scope.itemPath[10] = response["url_list"][6];
					        $scope.itemPath[11] = response["url_list"][7];
					        $scope.itemPath[12] = response["url_list"][10];
					        $scope.itemPath[13] = response["url_list"][11];
					        $scope.itemPath[14] = response["url_list"][12];
					        $scope.itemPath[15] = response["url_list"][13];
					        $scope.itemPath[16] = response["url_list"][15];
					        $scope.itemPath[17] = response["url_list"][16];
					        $scope.itemPath[18] = response["url_list"][17];

					        if(response["gender"][0]==2){
					        	$scope.gender="male";
					        } else {
					        	$scope.gender="femelle";
					        }
					        
					        for(var i=0; i<19; i++){
					        	$scope.itemId[i] = "https://fr.wowhead.com/item="+$scope.itemId[i];
					        	if($scope.itemPath[i]=="Defaut"){
					        		$scope.itemPath[i]="images/items/itemEmpty"+i+".png";
					        		document.getElementById('item'+i).style.border="2px solid #2F2F2F";
					        		console.log(document.getElementById('item'+i).style.border);

					        		var css = '#item'+i+':hover{ box-shadow: 0 0 1.2em #2F2F2F }';
									var style = document.createElement('style');
									if (style.styleSheet) {
										//console.log(style.styleSheet);
									    style.styleSheet.cssText = css;
									} else {
									    style.appendChild(document.createTextNode(css));
									}
									document.getElementsByTagName('head')[0].appendChild(style);
					        	}
					        }
					        //verif = true;
					        console.log($scope.race);
					        console.log($scope.gender);
					        $scope.loader = false;
					        $scope.error = false;
					        $scope.$apply();
					    }
					}
			    }
			};
			
			request.open("GET", "https://wowarmorybackend.herokuapp.com/data/?pseudo=" + $scope.pseudo + "&faction=" + $scope.faction + "&race=" + $scope.race);
			request.send();

			/*while(verif==false){
				await sleep(20);
			}*/



			/*console.log("scope.accueil: "+$scope.accueil);
			console.log("scope.armory: "+$scope.armory);
			console.log("scope.faction: "+$scope.faction);
			console.log("scope.background: "+$scope.background);*/
		} else {
			$scope.error=true;
			$scope.$apply();
		}
	};

	$scope.back = function(){
		$scope.armory = false;
		$scope.accueil= true;
		$scope.background={"background" : "url(images/accueil.png) no-repeat center center fixed",
		"-webkit-background-size" : "cover",
		"-moz-background-size": "cover",
		"-o-background-size" : "cover",
		"background-size" : "cover"
		};
		
		/*$scope.dataPlayer.clear();
		$scope.itemId.clear();
		$scope.itemPath.clear();*/
		$scope.$apply();
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

/*function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}*/
