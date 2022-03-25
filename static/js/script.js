
console.log('Hello World!')

const spinner = document.getElementById('spinner');
const list = document.getElementById('list');
console.log(spinner.classList)

$.ajax({
    type: 'GET',
    url: '/',
    success: function(res){
        setTimeout(()=>{
            // spinner.classList.add('invisible')
            console.log('success')
            list.innerHTML = `
            <div class="col-12 mt-3 left">
                <div class="row">
                {% for review in review_list %}         
                    <div class="col-md-3 col-sm-6 crd-box">
                    <a href="{% url 'review_content' review.slug %}" class="post-link">
                        <div class="review-container crd">
                            <div class="img-placement">
                            {% if "placeholder" in review.featured_image.url %}
                                <img class="review-img crd"
                                    src="https://static.turbosquid.com/Preview/2014/05/19__20_05_03/MovieCamera1SigWBG.jpg60d7c51a-b1b2-4266-93ed-2d47e3bf5a73Large.jpg">
                            {% else %}
                                <img class="review-img crd" 
                                    src=" {{ review.featured_image.url }}">
                            {% endif %}
                            </div>
                            <div class="info-placement bg-black-transparent white-txt">
                                <h5 class="card-title">{{ review.title }}</h5>
                                {% if review.rating == 1 %}
                                <p class="light-blue star"><i class="fa-solid fa-star"></i></p>
                                {% elif review.rating == 2 %}
                                <p class="light-blue star"><i class="fa-solid fa-star"></i>
                                    <i class="fa-solid fa-star"></i>
                                </p>
                                {% elif review.rating == 3 %}
                                <p class="light-blue star"><i class="fa-solid fa-star"></i>
                                    <i class="fa-solid fa-star"></i>
                                    <i class="fa-solid fa-star"></i>
                                </p>
                                {% elif review.rating == 4 %}
                                <p class="light-blue star"><i class="fa-solid fa-star"></i>
                                    <i class="fa-solid fa-star"></i>
                                    <i class="fa-solid fa-star"></i>
                                    <i class="fa-solid fa-star"></i>
                                </p>
                                {% else %}
                                <p class="light-blue star"><i class="fa-solid fa-star"></i>
                                    <i class="fa-solid fa-star"></i>
                                    <i class="fa-solid fa-star"></i>
                                    <i class="fa-solid fa-star"></i>
                                    <i class="fa-solid fa-star"></i>
                                </p>
                                {% endif %}
                                <hr/>
                                <p class="info">{{ review.created_date }} 
                                    <i class="far fa-heart"></i>{{ review.no_of_likes }} 
                                    <i class="far fa-comments"></i>{{ comments.no_of_comments }}</strong>
                                </p>
                        </div>
                    </div>
                    </a>
                </div>
                {% endfor %}
            </div>
            `
        },400)
    },
    error: function(er){
        console.log('error')
    },
})