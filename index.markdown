---
layout: page
---

<style>
    #head-image-wrapper {
        position: relative;
    }

    #head-image {
        width: 100%;
        z-index: 1;
    }

    .parent-link {
        position: absolute;
        cursor: pointer;
    }

    #michael-link {
        width: 25%;
        height: 40%;
        top: 9%;
        left: 29%;
    }

    #barbara-link {
        width: 25%;
        height: 35%;
        top: 24%;
        left: 61%;
    }

    @font-face {
      font-family: nyt-cheltenham;
      src: url('{{ site.baseurl }}/nyt-cheltenham-normal.ttf') format('truetype');
    }
    @font-face {
      font-family: nyt-cheltenham;
      font-weight: bold;
      src: url('{{ site.baseurl }}/nyt-cheltenham-bold.ttf') format('truetype');
    }
    body {
      font-family: nyt-cheltenham, sans-serif;
      font-size: 20px;
    }
    p {
        margin-top: 1rem;
    }
</style>

<h1 style='text-align: center; margin-top: -1em'>WHO DOESN'T LOVE OLD NEWS</h1>

<div id='head-image-wrapper'>
    <img src='momdad.png' id='head-image' />
    <a href='{{ site.baseurl }}/michael' class='parent-link' id='michael-link'> </a>
    <a href='{{ site.baseurl }}/barbara' class='parent-link' id='barbara-link'> </a>
</div>

<p>
    This website contains an archive of digitized articles written by <a href='{{ site.baseurl }}/barbara'>Barbara Slavin</a> and <a href='{{ site.baseurl }}/michael'>Michael Ross</a>, drawn from the following publications:
</p>

{% assign thresh = 20 %}
{% assign others = 0 %}
{% assign num_others = 0 %}
{% assign pubs = '' | split: '' %}
{% for a in site.data.barbara %}
    {% assign apubs = a.pub %}
    {% assign pubs = pubs | concat: apubs %}
{% endfor %}
{% for a in site.data.michael %}
    {% assign apubs = a.pub %}
    {% assign pubs = pubs | concat: apubs %}
{% endfor %}
{% assign pubs = pubs | sort_natural %}
{% assign current = pubs.first %}
{% assign num = 1 %}
<ul style='display: flex; flex-direction: column-reverse'>
    {% for pub in pubs %}
        {% assign pup = pub | upcase %}
        {% assign cup = current | upcase %}
        {% if pup == cup %}
            {% assign num = num | plus: 1 %}
        {% else %}
            {% if num >= thresh %}
                <li style='order: {{ num }}'><strong>{{ current }}</strong>: {{ num }} articles</li>
            {% else %}
                {% assign others = others | plus: num %}
                {% assign num_others = num_others | plus: 1 %}
            {% endif %}
            {% assign current = pub %}
            {% assign num = 1 %}
        {% endif %}
    {% endfor %}
    {% if num >= thresh %}
        <li style='order: {{ num }}'>{{ current }}: {{ num }} articles</li>
    {% else %}
        {% assign others = others | plus: num %}
        {% assign num_others = num_others | plus: 1 %}
    {% endif %}
    {% if num_others > 0 %}
        <li style='order: 0'>&hellip;and {{ num_others }} other publications with {{ others }} articles</li>
    {% endif %}
</ul>

Because many of the older digitized print articles contained errors stemming from imperfect optical character recognition, I used the <a href='https://github.com/Dicklesworthstone/llm_aided_ocr' target='_blank'><code>llm_aided_ocr</code></a> library with an OpenAI language model to make corrections. This error correction process, while surprisingly effective, is itself imperfect, so some inaccuracies may remain.
