FROM ruby:3.3.3

WORKDIR /GTFOBins/

COPY ./Gemfile ./
COPY ./Gemfile.lock ./

RUN bundle install

COPY ./ ./
