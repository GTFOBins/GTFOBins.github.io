FROM ruby:3.3.3

WORKDIR /site/

COPY ./Gemfile ./
COPY ./Gemfile.lock ./

RUN bundle install

COPY ./ ./site/
