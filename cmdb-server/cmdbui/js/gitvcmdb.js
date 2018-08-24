  $(function(){
        //按钮单击时执行
        $("#asset").click(function(){
                $.get("/front/asset.html", function(result){
                $('#mainbody').html(result);
            })
         });

        $("#dashboard").click(function(){

	        $.get("/front/dashboard.html", function(result){
        		  $('#mainbody').html(result);
       		 })

         });
	
	    $("#workflow").click(function(){
            $.get("/front/workflow.html", function(result){
                          $('#mainbody').html(result);
                 })
        
            $.get("/front/task.html", function(result){
                          $('#home').html(result);
            })
         });
        
        $("#manage").click(function(){

	        $.get("/front/manage.html", function(result){
        		  $('#mainbody').html(result);
       		 })

         });
	

        $.get("/auth/login/", function(result){
  	    $("#myuserid").html(result);
	});


      $('#tag-form').submit(function() {
        $.ajax({
            type: "POST",
            url: "/asset/update/",
            data: $('form.updateasset').serialize(),
            success: function(response) {
                $('#myModal').modal('hide');
                 alert('update');
                $('#example').DataTable().ajax.reload(null, false);

            },
            error: function() {
                alert('Error');
            }
        });
        return false;
    });

 });





