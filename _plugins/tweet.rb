# Author: Trevor Bedford
# License: MIT

# Examples:
#  {% tweet url description %}
#  {% tweet {{page.url}} {{page.title}} %}


module Jekyll
	class Tweet < Liquid::Tag
		def initialize(tag_name, markup, tokens)
			super
			@markup = "#{markup}".strip
		end
		def render(context)
		
			parsed = Liquid::Template.parse(@markup).render(context)
			url = (parsed.split(/ /).first || "").strip
			if url =~ /^\//
				url = "https://ccsb.pvamu.edu" + url
			end				
			text = (parsed.split(/ /).drop(1).join(' ') || "").strip
			url_encoded = url.gsub(/ /, '%20')
			text_encoded = text.gsub(/ /, '%20')
			html = "<i class=\"fa fa-twitter fa-fw\"></i> <a class=\"off\" href=\"https://twitter.com/share?url=#{url_encoded}&text=#{text_encoded}\" target=\"_blank\">tweet</a>"
			html 
			
		end
	end
end

Liquid::Template.register_tag('tweet', Jekyll::Tweet)