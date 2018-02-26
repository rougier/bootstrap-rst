.. html5-header::

   .. container:: navbar navbar-expand-md navbar-dark fixed-top bg-dark
      :tagname: nav

      .. container:: navbar-brand
	 :tagname: a
	 :attributes: href=#

	 Carousel

      .. container:: navbar-toggler
	 :tagname: button
	 :attributes: type=button
		      data-toggle=collapse
		      data-target=#navbarCollapse
		      aria-controls=navbarCollapse
		      aria-expanded=false
		      aria-label="Toggle navigation"

	 .. raw:: html

	    <span class="navbar-toggler-icon"></span>

      .. container:: collapse navbar-collapse
	 :attributes: id=navbarCollapse

	 .. raw:: html

	    <ul class="navbar-nav mr-auto">
	      <li class="nav-item active">
		<a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
	      </li>
	      <li class="nav-item">
		<a class="nav-link" href="#">Link</a>
	      </li>
	      <li class="nav-item">
		<a class="nav-link disabled" href="#">Disabled</a>
	      </li>
	    </ul>
	    <form class="form-inline mt-2 mt-md-0">
	      <input class="form-control mr-sm-2" type="text" placeholder="Search" aria-label="Search">
	      <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
	    </form>

.. container::
   :tagname: main
   :attributes: role=main

   .. carousel:: myCarousel
      :indicators: 3
      :control:

      .. carousel-item:: active

	 .. image:: data:image/gif;base64,R0lGODlhAQABAIAAAHd3dwAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==
	    :class: first-slide
	    :alt: First slide

	 .. container:: container

	    .. carousel-caption:: text-left

	       :h1:`Example headline.`

	       Cras justo odio, dapibus ac facilisis in, egestas eget quam. Donec id elit non mi porta gravida at eget metus. Nullam id dolor id nibh ultricies vehicula ut id elit.

	       .. button:: Sign up today
		  :class: large primary
		  :target: #

      .. carousel-item::

	 .. image:: data:image/gif;base64,R0lGODlhAQABAIAAAHd3dwAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==
	    :class: second-slide
	    :alt: Second slide

	 .. container:: container

	    .. carousel-caption::

	       :h1:`Another example headline.`

	       Cras justo odio, dapibus ac facilisis in, egestas eget quam. Donec id elit non mi porta gravida at eget metus. Nullam id dolor id nibh ultricies vehicula ut id elit.

	       .. button:: Learn more
		  :class: large primary
		  :target: #

      .. carousel-item::

	 .. image:: data:image/gif;base64,R0lGODlhAQABAIAAAHd3dwAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==
	    :class: third-slide
	    :alt: Third slide

	 .. container:: container

	    .. carousel-caption:: text-right

	       :h1:`One more for good measure.`

	       Cras justo odio, dapibus ac facilisis in, egestas eget quam. Donec id elit non mi porta gravida at eget metus. Nullam id dolor id nibh ultricies vehicula ut id elit.

	       .. button:: Browse gallery
		  :class: large primary
		  :target: #

   .. container:: container marketing

      .. row::

	 .. container:: col-lg-4

	    .. image:: data:image/gif;base64,R0lGODlhAQABAIAAAHd3dwAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==
	       :class: rounded-circle
	       :alt: Generic placeholder image
	       :width: 140
	       :height: 140

	    :h2:`Heading`

	    Donec sed odio dui. Etiam porta sem malesuada magna mollis euismod. Nullam id dolor id nibh ultricies vehicula ut id elit. Morbi leo risus, porta ac consectetur ac, vestibulum at eros. Praesent commodo cursus magna.

	    .. button:: View details &raquo;
	       :class: secondary
	       :target: #

	 .. container:: col-lg-4

	    .. image:: data:image/gif;base64,R0lGODlhAQABAIAAAHd3dwAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==
	       :class: rounded-circle
	       :alt: Generic placeholder image
	       :width: 140
	       :height: 140

	    :h2:`Heading`

	    Duis mollis, est non commodo luctus, nisi erat porttitor ligula, eget lacinia odio sem nec elit. Cras mattis consectetur purus sit amet fermentum. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh.

	    .. button:: View details &raquo;
	       :class: secondary
	       :target: #

	 .. container:: col-lg-4

	    .. image:: data:image/gif;base64,R0lGODlhAQABAIAAAHd3dwAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==
	       :class: rounded-circle
	       :alt: Generic placeholder image
	       :width: 140
	       :height: 140

	    :h2:`Heading`

	    Donec sed odio dui. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Vestibulum id ligula porta felis euismod semper. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus.

	    .. button:: View details &raquo;
	       :class: secondary
	       :target: #

   .. raw:: html

      <hr class="featurette-divider">

   .. container:: row featurette

      .. container:: col-md-7

	 .. container:: featurette-heading
	    :tagname: h2

	    First featurette heading.

	    .. raw:: html

	       <span class="text-muted">It'll blow your mind.</span>

	 .. container:: lead
	    :tagname: p

	    Donec ullamcorper nulla non metus auctor fringilla. Vestibulum id ligula porta felis euismod semper. Praesent commodo cursus magna, vel scelerisque nisl consectetur. Fusce dapibus, tellus ac cursus commodo.

      .. container:: col-md-5

	 .. container:: featurette-image img-fluid mx-auto
	    :tagname: img
	    :attributes: data-src="holder.js/500x500/auto"
			 alt="Generic placeholder image"
	    :endless:

   .. raw:: html

      <hr class="featurette-divider">

   .. container:: row featurette

      .. container:: col-md-7 order-md-2

	 .. container:: featurette-heading
	    :tagname: h2

	    Oh yeah, it's that good.


	    .. raw:: html

	       <span class="text-muted">See for yourself.</span>

	 .. container:: lead
	    :tagname: p

	    Donec ullamcorper nulla non metus auctor fringilla. Vestibulum id ligula porta felis euismod semper. Praesent commodo cursus magna, vel scelerisque nisl consectetur. Fusce dapibus, tellus ac cursus commodo.

      .. container:: col-md-5 order-md-1

	 .. container:: featurette-image img-fluid mx-auto
	    :tagname: img
	    :attributes: data-src="holder.js/500x500/auto"
			 alt="Generic placeholder image"
	    :endless:

   .. raw:: html

      <hr class="featurette-divider">

   .. container:: row featurette

      .. container:: col-md-7

	 .. container:: featurette-heading
	    :tagname: h2

	    And lastly, this one.

	    .. raw:: html

	       <span class="text-muted">Checkmate.</span>

	 .. container:: lead
	    :tagname: p

	    Donec ullamcorper nulla non metus auctor fringilla. Vestibulum id ligula porta felis euismod semper. Praesent commodo cursus magna, vel scelerisque nisl consectetur. Fusce dapibus, tellus ac cursus commodo.

      .. container:: col-md-5

	 .. container:: featurette-image img-fluid mx-auto
	    :tagname: img
	    :attributes: data-src="holder.js/500x500/auto"
			 alt="Generic placeholder image"
	    :endless:

   .. raw:: html

      <hr class="featurette-divider">

   .. html5-footer:: container

      .. container:: float-right
	 :tagname: p

	 `Back to top <#>`_

      .. raw:: html

	 <p>&copy; 2017 Company, Inc. &middot; <a href="#">Privacy</a> &middot; <a href="#">Terms</a></p>
