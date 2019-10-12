<template>
  <div id="user">
    <br>
   {{message}}
  </div>
</template>

<script>
	// 创建用户对象
	// let User = {
	// 	// 钩子data-作为对象User的属性
	export default {
		data: function() {
			return {
				message: '',
				iconlist: []
			};
		},
		onLoad: function() {
			this.getHomeInfo () 
			// console.log(this.message)
			console.log(this.iconList)
			console.log(this.message)
			
		},
		methods: {
			// uni.request写在methods中，便于复用，可以在其他属性中被调用
			getHomeInfo () {  
				uni.request({
					url: 'http://127.0.0.1:8000/test/', //仅为示例，并非真实接口地址。
					
					//   header: {
						// 'content-type': 'application/json'		
					//   },
					success: (res) => {
						const data = res.data.data
						console.log(this.iconList)
					// 	this.iconList = data.iconList //执行到这里会报错，因为iconList为定义
						console.log(this.iconList)
						this.message = res.data.message
						console.log(this.message)				
					}
				});
			}
		},
		mounted: function() {
			
		},
		
		created: function() {
			
		},
		computed: {
			
		}		
	}

</script>

<stype scoped>

</stype>
