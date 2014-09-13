var scraps = 0;
var ScrapBots = 0;
var ScrapBotCost = 10;

function scrapClick(number){
    scraps = scraps + number;
    document.getElementById("scraps").innerHTML = scraps; 
};


function buyScrapBot(){
    ScrapBotCost = Math.floor(10 * Math.pow(1.1,ScrapBots));     //works out the cost of this cursor
    if(scraps >= ScrapBotCost){                                   //checks that the player can afford the cursor
        ScrapBots = ScrapBots + 1;                                   //increases number of cursors
    	scraps = scraps - ScrapBotCost;                          //removes the cookies spent
        document.getElementById('ScrapBots').innerHTML = ScrapBots;  //updates the number of cursors for the user
        document.getElementById('scraps').innerHTML = scraps;  //updates the number of cookies for the user
    };
    ScrapBotCost = Math.floor(10 * Math.pow(1.1,ScrapBots));
    document.getElementById('ScrapBotCost').innerHTML = ScrapBotCost;  //updates the cursor cost for the user	
};

window.setInterval(function(){
	scrapClick(ScrapBots);
}, 1000);

function save(){

    var save = {
        scraps: scraps,
        ScrapBots: ScrapBots,
        ScrapBotCost: ScrapBotCost
    };

    localStorage.setItem("save",JSON.stringify(save)); 
};

function load(){
    var savegame = JSON.parse(localStorage.getItem("save")); 
    if (typeof savegame.scraps !== "undefined") scraps = savegame.scraps;
    if (typeof savegame.ScrapBots !== "undefined") ScrapBots = savegame.ScrapBots;
    if (typeof savegame.ScrapBotCost !== "undefined") ScrapBotCost = savegame.ScrapBotCost;

    document.getElementById('ScrapBots').innerHTML = ScrapBots;  
    document.getElementById('scraps').innerHTML = scraps;
    document.getElementById('ScrapBotCost').innerHTML = ScrapBotCost;
};
