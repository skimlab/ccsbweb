# Author: Trevor Bedford
# License: MIT

# Examples:
#  {% trackback url %}
#  {% trackback {{page.url}} %}

require 'json'
require 'open-uri'

module Jekyll
	class Trackback < Liquid::Tag
		def initialize(tag_name, markup, tokens)
			super
			@markup = "#{markup}".strip
		end
		def render(context)
			# Twitter count API was deprecated and shut down; return empty string to prevent build crash
			""
		end
	end
end

Liquid::Template.register_tag('trackback', Jekyll::Trackback)