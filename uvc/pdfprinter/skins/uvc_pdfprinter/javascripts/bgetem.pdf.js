(function ($) {


  'use strict';

  function print_tabs () {
    var $tab_panes = $(".tab-content .tab-pane");
    $("#content .nav-tabs li").each( function(index, element) {
      var tab_heading = "";
      var content = $(this).text();
      if(content) {
        tab_heading += "<h4>" + content + "</h4>";
      }
      $tab_panes.eq(index).prepend(tab_heading);
    });
  };

  if (window.matchMedia) {
        var mediaQueryList = window.matchMedia('print');
        mediaQueryList.addListener(function(mql) {
            if (mql.matches) 
	    	print_tabs();
        });
}
  
}(jQuery));
