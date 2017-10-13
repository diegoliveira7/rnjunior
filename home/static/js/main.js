/* ========================================================================= */
/*	Preloader
/* ========================================================================= */

jQuery(window).load(function(){

	$("#preloader").fadeOut("slow");

});

/* ========================================================================= */
/*  Welcome Section Slider
/* ========================================================================= */

$(function() {

    var Page = (function() {

        var $navArrows = $( '#nav-arrows' ),
            $nav = $( '#nav-dots > span' ),
            slitslider = $( '#slider' ).slitslider( {
                onBeforeChange : function( slide, pos ) {

                    $nav.removeClass( 'nav-dot-current' );
                    $nav.eq( pos ).addClass( 'nav-dot-current' );

                }
            } ),

            init = function() {

                initEvents();
                
            },
            initEvents = function() {

                // add navigation events
                $navArrows.children( ':last' ).on( 'click', function() {

                    slitslider.next();
                    return false;

                } );

                $navArrows.children( ':first' ).on( 'click', function() {
                    
                    slitslider.previous();
                    return false;

                } );

                $nav.each( function( i ) {
                
                    $( this ).on( 'click', function( event ) {
                        
                        var $dot = $( this );
                        
                        if( !slitslider.isActive() ) {

                            $nav.removeClass( 'nav-dot-current' );
                            $dot.addClass( 'nav-dot-current' );
                        
                        }
                        
                        slitslider.jump( i + 1 );
                        return false;
                    
                    } );
                    
                } );

            };

            return { init : init };

    })();

    Page.init();

});
var selecionado=null
var servicoSelecionado=null
$(document).ready(function(){
    
    $( window ).load( function(){
        $( '.lazyload' ).each( function(){
            //* set the img src from data-src
            $( this ).attr( 'src', $( this ).attr( 'data-src' ) );
        } );
        $( '.lazyloadBackground' ).each( function(){
            //* set the img src from data-src
            $( this ).css( 'background-image','url('+ $( this ).attr( 'data-src' )+")" );
        } );
        equipeInicial=$("#equipe-completa").html()
    } );

    $('.openModalContrateSuaEj').click(function() {
        $('#referenciaContrateUmaEJ').text('Contato com a empresa '+$(this).attr( "empresa" )+" em relação ao serviço "+servicoSelecionado) 
        $('#myModal').modal('show')   
    })

    $('.equipe-pessoa-select').click(function() {
        if(selecionado?$(this)[0].id!==selecionado[0].id:true){
            selecionado=$(this)
            $(this).parent().toggleClass("col-xs-12")
            $(this).parent().toggleClass("col-md-3")
            $(this).parent().toggleClass("col-xs-6")
            $("."+$(this)[0].id).css("display","block")
            $("#voltar-equipe-completa").css("display","flex")
            $("#equipe-completa").children().css("display","none")
            $(this).parent().css("display","block")
        }
    })
    $("#voltar-equipe-completa").click(function() {
        if(selecionado){
            $("."+selecionado[0].id).css("display","none")
            selecionado.parent().toggleClass("col-xs-6")
            selecionado.parent().toggleClass("col-md-3")
            selecionado.parent().toggleClass("col-xs-12")
            $("#voltar-equipe-completa").css("display","none")
            $("#equipe-completa").children().css("display","inline-block")
            selecionado=null
        }
    })
    // Contrate sua ej
    var $areas = $('#contrateSuaEjArea').change(function() {
        $('#contrateSuaEjServico').val("0");
        var id=$('#contrateSuaEjArea').find(":selected")[0].id
        if (id == 'area-none') {
            $('#contrateSuaEjServico > option').hide();
            $('#empresas-selecionadas > div').removeClass('displayNodeServico');
        } else {
            var $el = $('.' + id)
            $('#empresas-selecionadas > div').removeClass('displayNodeServico');
            $('#empresas-selecionadas > div').not($el).addClass('displayNodeServico');

            $("#contrateSuaEjServico > ."+id).show();
            $("#contrateSuaEjServico > option").not($el).hide();
        }
    })
    var $servicos = $('#contrateSuaEjServico').change(function() {
        var id=$('#contrateSuaEjServico').find(":selected")[0].id
        servicoSelecionado=id;
        if (id == 'servico-none') {
            $('#contrateSuaEjServico > option').addClass('displayNodeServico');
            $('#empresas-selecionadas > div').removeClass('displayNodeServico');
        } else {
            var $el = $('.' + id)
            $('#empresas-selecionadas > div').removeClass('displayNodeServico');
            $('#empresas-selecionadas > div').not($el).addClass('displayNodeServico');
        }
    })



	/* ========================================================================= */
	/*	Menu item highlighting
	/* ========================================================================= */

	jQuery('#nav').singlePageNav({
		offset: jQuery('#nav').outerHeight(),
		filter: ':not(.external)',
		speed: 2000,
		currentClass: 'current',
		easing: 'easeInOutExpo',
		updateHash: true,
		beforeStart: function() {
			console.log('begin scrolling');
		},
		onComplete: function() {
			console.log('done scrolling');
		}
	});
	
    $(window).scroll(function () {
        if ($(window).scrollTop() > 400) {
            $(".navbar-brand a").css("color","#fff");
            $("#navigation").removeClass("animated-header");
        } else {
            $(".navbar-brand a").css("color","inherit");
            $("#navigation").addClass("animated-header");
        }
    });
	
	/* ========================================================================= */
	/*	Fix Slider Height
	/* ========================================================================= */	

    // Slider Height
    var slideHeight = $(window).height();
    
    $('#home-slider, #slider, .sl-slider, .sl-content-wrapper').css('height',slideHeight);

    $(window).resize(function(){'use strict',
        $('#home-slider, #slider, .sl-slider, .sl-content-wrapper').css('height',slideHeight);
    });
	
	
	
	$("#works, #testimonial").owlCarousel({	 
		navigation : true,
		pagination : false,
		slideSpeed : 700,
		paginationSpeed : 400,
		singleItem:true,
		navigationText: ["<i class='fa fa-angle-left fa-lg'></i>","<i class='fa fa-angle-right fa-lg'></i>"]
	});
	
	
	/* ========================================================================= */
	/*	Featured Project Lightbox
	/* ========================================================================= */

	$(".fancybox").fancybox({
		padding: 0,

		openEffect : 'elastic',
		openSpeed  : 650,

		closeEffect : 'elastic',
		closeSpeed  : 550,

		closeClick : true,
			
		beforeShow: function () {
			this.title = $(this.element).attr('title');
			this.title = '<h3>' + this.title + '</h3>' + '<p>' + $(this.element).parents('.portfolio-item').find('img').attr('alt') + '</p>';
		},
		
		helpers : {
			title : { 
				type: 'inside' 
			},
			overlay : {
				css : {
					'background' : 'rgba(0,0,0,0.8)'
				}
			}
		}
	});
	
});

// ========== END GOOGLE MAP ========== //

var wow = new WOW ({
	offset:       75,          // distance to the element when triggering the animation (default is 0)
	mobile:       false,       // trigger animations on mobile devices (default is true)
});
wow.init();