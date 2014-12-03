$(function() {
  // This is our model
  groups = {
    "good":{"ui":"#fruits-good","values":[]},
    "bad":{"ui":"#fruits-bad","values":[]},
    "none":{"ui":"#fruits-stickers","values":[]},
    "pgood":{"ui":"#fruits-pgood","values":[]},
    "pbad":{"ui":"#fruits-pbad","values":[]}
  }
  // Append a fruit to a new group 
  function appendTo(ui, key){
    // Get the name of the group and the fruit
    destGroup = groups[key]
    itemVal = ui.draggable.text();
    // UI effect
    ui.draggable.fadeOut();
    // Remove from previous group
    _.each(groups,function(d){
      var index = d.values.indexOf(itemVal)
      if (index > -1) { d.values.splice(index,1); }
    });
    // Add to new group and redraw
    destGroup.values.push(itemVal)
    drawGroups(); 
  };
 
  // Main drawing function to redraw UI from logic
  function drawGroups(){

    // Build a fruit HTML node
    function buildFruit( n){ return "<div class='draggable'>"+n+"</div>"; };
    // Update the count of unused element
    function updateCounts(){ $("#none-count").text(groups.none.values.length);}
    
    // Draw each group
    _.each(groups, function(group){
      $(group.ui).text("");
      _.each(group.values, function(element){
        $(group.ui).append(buildFruit(element));
      });
    });
    
    // Rebind the draggable feature
    $( ".draggable" ).draggable();
    updateCounts()
  }
  
  // To requery the server for a new list and reset all the UI
  function reset(){
    $.get("list", function(data){
      // Clean previous data 
      _.each(groups, function(d){d.values = [] ;})
      // Parse new data and redraw
      groups["none"]["values"] = JSON.parse(data);
      drawGroups()
      
      // Set up the drag and drop behavior
      $( "#happy" ).droppable({ drop: function( e, ui ) { appendTo(ui,"good"); }});
      $( "#sad" ).droppable({ drop: function( e, ui ) { appendTo(ui,"bad"); }});
    });
  }

  $('#reset').click(function(d){ reset(); }); 
  $('#launch').click(function(d){
    $.post( "run", encodeURIComponent(JSON.stringify(groups)))
      .done(function( data ) { 
        groups = JSON.parse(data)
        drawGroups();
      });
  });
 

  reset();
});

