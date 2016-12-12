(function ($) {

  'use strict';

  function print_tabs () {
    var $tab_panes = $(".tab-content .tab-pane");
    $("#content .nav-tabs li").each( function(index, element) {
      var tab_heading = "";
      var content = $(this).text();
      if(content) {
        tab_heading += "<h4 class='visible-print-block'>" + content + "</h4>";
      }
      $tab_panes.eq(index).prepend(tab_heading);
    });
  };
  function printListener (mql) {
    if (mql.matches) {
      print_tabs();
      mediaQueryList.removeListener(printListener);
    }
  }
  if (window.matchMedia) {
    var mediaQueryList = window.matchMedia('print');
    if(mediaQueryList.matches) {
      print_tabs();
      mediaQueryList.removeListener(printListener);
    }
    else {
      mediaQueryList.addListener(printListener);
    }
  }
  
}(jQuery));
