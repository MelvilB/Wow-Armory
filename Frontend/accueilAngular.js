var app = angular.module("Accueil", []);

app.controller("globalController", function($scope){
	$scope.pseudo="";
	$scope.user="";
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
	$scope.error= [false, false, false];
	$scope.showLogin=false;

	$scope.get = async function(faction){
		$scope.error[1]=false;
		$scope.error[2]=false;
		var raceAlliance = ["Gnome", "Humain", "Elfe de la nuit", "Nain"];
		var raceHorde = ["Orc", "Mort-vivant", "Tauren", "Troll"];
		if($scope.pseudo.length >= 2 && $scope.pseudo.length <= 12){
			if($scope.race=="" || faction=="Alliance" && raceAlliance.indexOf($scope.race)===-1 || faction=="Horde" && raceHorde.indexOf($scope.race)===-1){
				$scope.error[0]=true;
				$scope.back();
			} else {
				$scope.faction = faction;
				$scope.loader = true;
				$scope.$apply();

				var request = new XMLHttpRequest();
				var verif = false;

				request.onreadystatechange = function() {
					if (this.readyState == XMLHttpRequest.DONE && this.status == 200) {
				        var response = JSON.parse(this.responseText);
				        $scope.dataPlayer=response;
				        
				        if($scope.dataPlayer['name']=="introuvable"){
				        	$scope.loader = false;
				        	$scope.error[0]=true;
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
									    style.styleSheet.cssText = css;
									} else {
									    style.appendChild(document.createTextNode(css));
									}
									document.getElementsByTagName('head')[0].appendChild(style);
					        	}
					        }
					        $scope.loader = false;
					        $scope.error[0] = false;
					        $scope.$apply();
					    }
					}
			    }
			};
			request.open("GET", "https://wowarmorybackend.herokuapp.com/data/?pseudo=" + $scope.pseudo + "&faction=" + $scope.faction + "&race=" + $scope.race + "&user=" + $scope.user);
			request.send();
		} else {
			$scope.error[0] = true;
			$scope.$apply();
		}
	};

	$scope.back = function(){
		$scope.armory = false;
		$scope.accueil= true;
		$scope.background = {"background" : "url(images/accueil.png) no-repeat center center fixed",
		"-webkit-background-size" : "cover",
		"-moz-background-size": "cover",
		"-o-background-size" : "cover",
		"background-size" : "cover"
		};
		$scope.$apply();
	};

	$scope.accountCreation = function(){
		var pseudoInput = document.getElementById('pseudoInput').value;
		var passwordInput = document.getElementById('passwordInput').value;
		var passwordInputConf = document.getElementById('passwordInputConf').value;
		console.log(pseudoInput);
		console.log(passwordInput);
		console.log(passwordInputConf);
		$scope.error[0]=false;
		$scope.error[1]=false;
		$scope.error[2]=false;
		if(passwordInput != passwordInputConf || passwordInput== "" || pseudoInput== "" || passwordInputConf== ""){
			console.log("erreur");
			$scope.error[1] = true;
		} else {
			$scope.loader = true;
			var request = new XMLHttpRequest();
			request.onreadystatechange = function() {
				if (this.readyState == XMLHttpRequest.DONE && this.status == 200) {
			        var response = JSON.parse(this.responseText);
			        if(response["login"] == "echec"){
			        	$scope.error[1] = true;
			        } else {
			        	$scope.showLogin = false;
			        	$scope.error[2] = true;
			        }
			        $scope.loader = false;
			        $scope.$apply();
			    }
			}
			request.open("GET", "https://wowarmorybackend.herokuapp.com/login/?pseudoInput=" + pseudoInput + "&passwordInput=" + passwordInput);
			request.send();
		}
		$scope.accountClear();
	}

	$scope.accountClear = function(){
		document.getElementById('pseudoInput').value = "";
		document.getElementById('passwordInput').value = "";
		document.getElementById('passwordInputConf').value = "";
		$scope.$apply();
	}

});