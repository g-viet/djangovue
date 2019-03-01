import axios from 'axios'

export default class ModelService {
  sayHello () {
    return axios.get('http://localhost:8000/api/say_hello/', {headers: {}}).then((response) => {
      return response.data || 'default value'
    })
  }
}
