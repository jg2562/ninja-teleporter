console.log("This is an object... i think");
// Author -Grant 
function Person(name,health,cooldown,pos){
    this.name = name;
    this.health = health;
    this.cooldown = cooldown;
    this.pos = pos;

    this.damage = function(damage){
      this.health -= damage;
      if (this.health < 0){
        this.health = 0;
      }
    }

    this.get_pos = function(){
      return this.pos;
    }

    this.set_pos = function(pos){
      this.pos = pos;
    }
}

Warrior.prototype = new Person();
Warrior.prototype.constructor = Warrior;

function Warrior(name,health,cooldown,pos){
  this.name = name;
  this.healt = health;
  this.cooldown = cooldown;
  this.pos = pos;

  this.attack_area = [[0, 0, .5, 0, 0],[0, 2, 3, 2, 0],[.5, 1, 0, 1, .5],[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]];

  this.get_attack_area = function(){
    return this.attack_area;
  }
}

Baller.prototype = new Person();
Baller.prototype.constructor = Baller;

function Baller(name,health,cooldown,pos){
  this.name = name;
  this.healt = health;
  this.cooldown = cooldown;
  this.pos = pos;
  this.attack_area=  [[0, 1, 4, 1, 0],[0, 1, 4, 1, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]];
}

Child.prototype = new Person();
Child.prototype.constructor = Child;

function Child(name,health,cooldown,pos){
  this.name = name;
  this.healt = health;
  this.cooldown = cooldown;
  this.pos = pos;
  this.attack_area = [[1, 1, 1, 1, 1],[1, 1, 1, 1, 1], [1, 1, 1, 1, 1],[1, 1, 1, 1, 1], [1, 1, 1, 1, 1]];
}

Teliporta.prototype = new Person();
Teliporta.prototype.constructor = Teliporta;

function Teliporta(name,health,cooldown,pos){
  this.name = name;
  this.healt = health;
  this.cooldown = cooldown;
  this.pos = pos;

  this.attack_area = [[0, 0, 0, 0, 0],[0, 1, 8, 1, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]];
}

Zeus.prototype = new Person();
Zeus.prototype.constructor = Zeus;

function Zeus(name,health,cooldown,pos){
  this.name = name;
  this.healt = health;
  this.cooldown = cooldown;
  this.pos = pos;

  this.attack_area = get_attack_area();

  this.get_bolt_cords = function(){
    // where is size declared?
    return [Math.floor(Math.random() * this.size )+ 0];
  }

  this.get_attack_area = function(){
    var attack_area = [[],[]] ;
    for(var i = 0; i< 5; i++){
      for(var j = 0; j < 5; j++){
          attack_area[i][j] = 0;
      }
    }
    Cords = this.get_bolt_cords();
    this.attack_area[Cords[0],Cords[1]] = 50;
    return attack_area;
  }
}


function Game(size){
  this.size = (size,size,size);
  this.board = {};

  this.build_traps = function(test){
    return;
  }

  this.place_players = function(){
    return;
  }

  this.run = function(){
    return;
  }

  this.get_rand_cords = function(){
    return [(Math.floor(Math.random() * this.size )+ 0),(Math.floor(Math.random() * this.size )+ 0), 0 ,(Math.floor(Math.random() * 4 )+ 0)];

  }

  this.set_person = function(pos, player){
    this.board[player.get_pos()] = player;
  }

  this.get_player = function(pos){
    return this.board[this.pos[0],this.pos[1],this.pos[2]];
  }

  this.move_person = function(person,dpos){
    pos = person.get_pos();
    new_pos = (pos[0] + dpos[0], pos[1] + dpos[1], pos[2] + dpos[2]);
    this.set_person(new_pos);
  }

  this.attack_person = function(damage,pos){
    person = this.get_player(pos);
    if(person === "undefined"){
      return null;
    }
    // attack is defined where?
    person.damage(attack);
  }

  this.attack_area = function(pos){
    // where is get_person defined?
    person = get_person(pos);
    if (person === "undefined"){
      return null;
    }
    area = person.get_attack_area();
    height = area.length;
    width = area[0].length;
    for(var col = 0; col < height; col++){
      for(var row = 0; row < width; row++){
        this.attack_person(area[col][row], (pos[0] + (row - width/2), pos[1] + (col - height/2), 0));
      }
    }
  }
// have to place after defined above
  this.build_traps();
  this.place_players();
  this.run();

}

var G = new Game(10);
// console.log(G);
console.log(G.get_rand_cords());
