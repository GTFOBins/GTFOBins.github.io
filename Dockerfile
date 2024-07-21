FROM ruby:3.3.4

WORKDIR /GTFOBins/

COPY ./Gemfile ./
COPY ./Gemfile.lock ./

RUN bundle install

COPY ./ ./
