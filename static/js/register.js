/*
 * @Author: alexthezhang228 zhangy32@tcd.ie
 * @Date: 2023-02-21 08:01:10
 * @LastEditors: alexthezhang228 zhangy32@tcd.ie
 * @LastEditTime: 2023-02-25 21:37:16
 * @FilePath: /flask_project/static/js/register.js
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 */
function bindEmailCode(){
  $('#getCode').click(function(evt){
    var button_val=$(this)
    evt.preventDefault()
    var email=$("input[name='email']").val()
    $.ajax({
      url:'/author/captcha/email?email='+email,
      type:'GET',
      success:function(result){
        console.log(result)
        var code=result['code']
        if (code==200){
          alert('send successfully')
          button_val.off('click')
          var countdown=60
          var timer=setInterval(()=>{
            button_val.text(countdown)
            countdown-=1
            if (countdown<=0){
              clearInterval(timer)
              button_val.text('get code')
              bindEmailCode()
            }
          },1000)
        }else{
          alert(result['message'])
        }
      },
      fail:function(error){
        console.log(error)
      }
    })

  })
}

$(document).ready(
  $(function(){
  bindEmailCode()
}))
