$(function(){
	$("select#company").bind("change",setCompanyName);
	$(".pane").bind("mouseover",autoShow);
	$(".pane").bind("mouseout",autoHide);
	$(window).on("resize",sizeNav);

	autoHide();
	sizeNav();
});

function setCompanyName(){
	$val = $(this).val();
	if(!isNaN($val) && $val.indexOf("add_") == -1)
		$("input#sel_company_name").val($.trim($(this).children("option:selected").text()));
}

function autoHide(){
	setTimeout(function(){
		$(".autohide").animate({"height":"3px"},1000);
	},3000);
}

function autoShow(){
	$(".autohide").animate({"height":"50px"},1000);
}

function sizeNav(){
	var tabs = $(".core_nav ul li");
	var win_width = $(window).width() - 30;
	
	tabs.css({"width": (win_width / tabs.length )+ "px" });
}