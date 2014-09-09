var scraps = 0;

function scrapClick(number){
    scraps = scraps + number;
    document.getElementById("scraps").innerHTML = scraps; 
};

var ScrapBots = 0;

function buyScrapBot(){
    var ScrapBotCost = Math.floor(10 * Math.pow(1.1,ScrapBots));     //works out the cost of this cursor
    if(scraps >= ScrapBotCost){                                   //checks that the player can afford the cursor
        ScrapBots = ScrapBots + 1;                                   //increases number of cursors
    	scraps = scraps - ScrapBotCost;                          //removes the cookies spent
        document.getElementById('ScrapBots').innerHTML = ScrapBots;  //updates the number of cursors for the user
        document.getElementById('scraps').innerHTML = scraps;  //updates the number of cookies for the user
    };
    var nextCost = Math.floor(10 * Math.pow(1.1,ScrapBots));       //works out the cost of the next cursor
    document.getElementById('ScrapBotCost').innerHTML = nextCost;  //updates the cursor cost for the user	
};

window.setInterval(function(){
	scrapClick(ScrapBots);
}, 1000);

function save(){

    var save = {
        scraps: scraps,
    };

    var save2 = {
        ScrapBots: ScrapBots,
        ScrapBotCost: ScrapBotCost,
    };

    localStorage.setItem("save",JSON.stringify(save)); 
};

function load(){
    var savegame = JSON.parse(localStorage.getItem("save")); 
    if (typeof savegame.scraps !== "undefined") scraps = savegame.scraps;
    if (typeof savegame.ScrapBots !== "undefined") ScrapBots = savegame.ScrapBots;
    if (typeof savegame.ScrapBotCost !== "undefined") ScrapBotCost = savegame.ScrapBotCost;

};