//Variable Declarations
const Discord = require('discord.js');
const bot = new Discord.Client();
const TOKEN = "";
const PREFIX = "!";

//On Succesful Turn On Message
bot.on('ready', function(){
    console.log('Sakura is ready');
});


//Command List
bot.on('message' ,function(message){
    if(message.author.equals(bot.user)) return;

    if(message.content == "Hello Sakura"){
        message.channel.sendMessage("Hello Senpai!");
    }
    if(!message.content.startsWith(PREFIX)) return;

    var args = message.content.substring(PREFIX.length).split(" ");

    switch(args[0].toLowerCase()){
        case "ping":
            message.channel.sendMessage("Pong");
            break;
        case "info":
            message.channel.sendMessage("Hello Senpai, my name is Sakura. Pleased to meet you ^.^");
            break;

        case "noticeme":
            message.channel.sendMessage(message.author.toString() + " Thats my line Senpai!");
            break;

        case "rank":
          if (args.length != 3){
            message.channel.send("Senpai its like this,  '!rank Summonername Region'.");

            break;
          }
          var spawn = require("child_process").spawn;
          var process = spawn('python',["summonerInfo.py", args[1], args[2]]);
          process.stdout.on('data',function(chunk){
            var textChunk = chunk.toString('utf8');// buffer to string
            message.channel.send(textChunk);
          });
          break;
        //Live currently not implemented properly
        case "live":
          var spawn = require("child_process").spawn;
          var process = spawn('python',["datagathering.py", args[1], args[2]]);
          process.stdout.on('data',function(chunk){
            var textChunk = chunk.toString('utf8');// buffer to string
            message.channel.sendMessage(textChunk);
          });
          break;

        case "help":
            var embed = new Discord.RichEmbed()
                .setDescription("Hello " + message.author.toString() + ", here are some of my commands")
                .addField("!ping", "I will respond with Pong", true)
                .addField("!info", "I will give you some information about me", true)
                .addField("!noticeme", "I'll get angry at you!", true)
            message.channel.sendEmbed(embed);
            break;
        default:
            message.channel.sendMessage("Sorry Senpai, I don't understand that command.");
    }
});

bot.login(TOKEN)
