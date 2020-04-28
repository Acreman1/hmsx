;

var user_edit_ops = {
    init:function(){
        this.eventBind()
    },
    eventBind:function(){
        $(".user_edit_wrap .save").click(function(){
            var btn_target = $(this)
            if (btn_target.hasClass("disabled")) {
                alert("请求正在进行，请稍后再试")
                return
            }
            var nickname_value = $(".user_edit_wrap input[name=nickname").val()
            var email_value = $(".user_edit_wrap input[name=email").val()

            if (!nickname_value || nickname_value.length < 2) {
                alert("昵称格式有误")
                return false;
            }

            if (!nickname_value || nickname_value.length < 2) {
                alert("邮箱格式有误")
                return false;
            }

            btn_target.addClass("disabled")

            $.ajax({
                url:common_ops.buildUrl("/user/edit"),
                type:"POST",
                data:{"nickname":nickname_value,"email":email_value},
                dataType:"json",
                success:function(resp){
                    common_ops.alert("ok！")
                    console.log(resp.msg)
                    btn_target.removeClass("disabled")
                },
                error:function(error){
                    console.log(error)
                    common_ops.alert("修改失败")
                }
            })
        })
    }
}

$(document).ready(function(){
    user_edit_ops.init()
})