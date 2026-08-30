# Author: Trevor Bedford
# License: MIT

module Jekyll
	class EqInline < Liquid::Tag
		def initialize(tag_name, markup, tokens)
			super
			@markup = "#{markup}".strip
		end
		def render(context)

			require 'execjs'

			parsed = Liquid::Template.parse(@markup).render context
			
			katex_path = File.expand_path("../../js/katex.min.js", __FILE__)
			katexsrc = File.read(katex_path)
			@katex = ExecJS.compile(katexsrc)
			return eqn_to_html(parsed)

		end
		def eqn_to_html(string)
			return @katex.call("katex.renderToString", string)
		end
	end
end

Liquid::Template.register_tag('eqinline', Jekyll::EqInline)
