// Home.vue

<template>
    <div>
        <p>Home page</p>
        <p>Random number from backend: {{ randomNumber }}</p>
        <button @click="getRandom">New random number</button>
	</div>
</template>

<script>
import Math from 'math'
import axios from 'axios'
export default{

	data(){
		return {
			randomNumber:0
		}
	},
	methods: {
		getRandom (){
		this.randomNumber = this.getRandomFromBackend()
		},
		getRandomFromBackend (){
			const path = 'http://localhost:5000/api/random'
			axios.get(path)
			.then(response =>{
				this.randomNumber = response.data.randomNumber
				console.log(response)
			})
			.catch(error => {
				console.log(error.response)
			})
		}
	},
	created () {
		this.getRandom()
	}
}
</script>
